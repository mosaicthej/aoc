#!/usr/bin/python

import itertools, operator
from typing import List

n=int(input())

s=0

def expbuild(exps, accu):
    return (exps if not accu else expbuild(exps[1:], accu+exps.jon))

def leftjoin(e1:str, e2:str) -> str: # '22+', '32*'; '(22+32)+', '67+'
    return ('(' +
            e1 + 
            (e2[:-1] if e2[-1] in '+*' else e2 )+
            ')' +
            (e2[-1] if e2[-1] in '+*' else ''))


def stackmachine(accu:int, last_op, # init with: accu=0, op=+
                 rest:tuple[tuple[int,int]]): # ((1,'+'), (3,'|'), (3,None))
    if not rest:
        return accu # base case, when done
    else: 
        if last_op == '+':
            ac = accu+rest[0][0]
        elif last_op == '*':
            ac = accu*rest[0][0]
        else: # last_op == '|':
            ac = int(str(accu)+str(rest[0][0]))
        return stackmachine(ac, rest[0][1], rest[1:])

for _ in range(n):
    exps = []
    r,ex = input().split(': ')
    r,nus =int(r), ex.split(' ')
    oss = itertools.product('+*|',repeat=len(nus)-1)
    
    # exps=[''.join(tuple( map(lambda x: operator.add(x[0],x[1]) if x[1] else x[0],
      #          itertools.zip_longest(nus, os))
       #     )) for os in oss]

    for os in oss:
        t0 = tuple(itertools.zip_longest(map(int,nus), os))
        res = stackmachine(0,'+',t0)
        if res==r:
            print(t0)
            s+=res
            break
print(s)


