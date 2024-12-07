#!/usr/bin/python
import operator, itertools
n=int(input())

Pos=tuple[int, int]
mat = [input() for _ in range(n)]
dirs = [d for d in itertools.product(range(-1,2), repeat=2)]

def findall(s:str, c:str, t:int):
    return [] if s=='' else ([t]+findall(s[1:],c,t+1) if s[0]==c else 
                             findall(s[1:],c,t+1))
# match something in given offsets
def match_diff(mat:list[str], 
               currPos:Pos, 
               diff:Pos, targ:str)-> bool:
    return (len(targ)==0 or # true if targ is empty
            (currPos[0]>=0 and currPos[0]< n and 
             currPos[1]>=0  and currPos[1]< len(mat[0]) and
             mat[currPos[0]][currPos[1]] == targ[0] and
                            match_diff(mat, 
                                       tuple(map(operator.add,currPos,diff)),
                                       diff, targ[1:])))

# this is all the locations that a search starts
all_xs = list(filter(lambda p: p[1], 
                     zip((m for m in range(n)),
                         map(lambda s: findall(s,'X',0), mat))))

# initiate this on all locations
truths=[match_diff(mat, curr, dif, 'XMAS') 
 for curr in (
     cp for cps in (itertools.product([m[0]],m[1]) for m in all_xs) 
     for cp in cps)
 for dif in dirs]

print(sum([1 if m else 0 for m in truths]))
