#!/usr/bin/python
from fractions import Fraction as fr

# [ a b | c
#   d e | f ]

def solve_claw(mat: tuple[tuple[int, int, int], 
                          tuple[int, int, int]]) -> tuple[int, int]:
    ((a,b,c), (d,e,f)) = mat
    a,b,c,d,e,f = map(fr, (a,b,c,d,e,f))
    
    B = ((d/a*c)-f) / (((d/a)*b)-e)
    A = (c-(B*b)) / a
    
    return (int(A), int(B)) if A.is_integer() and B.is_integer() else (-1, -1)


def claw_to_cost(claws:tuple[int,int])->int:
    return 3*claws[0]+claws[1] if claws[0]>-1 else 0


# ((34/94)*8400-5400)/(34/94*22 - 67)
# ((fr(34)/fr(94))*fr(8400)-fr(5400))/(fr(34)/fr(94)*fr(22) - fr(67)) 

CORR=10000000000000
n = int(input())
tokens = 0
for i in range(n):
    Xa, Ya = map(lambda s: int(s.split('+')[-1]), input().split(','))
    Xb, Yb = map(lambda s: int(s.split('+')[-1]), input().split(','))
    X, Y = map(lambda s: int(s.split('=')[-1])+CORR, input().split(','))
    input()
    this_claw = claw_to_cost(
            solve_claw(((Xa,Xb,X),
                        (Ya,Yb,Y))))
    print(this_claw)
    tokens += this_claw
print(tokens)



