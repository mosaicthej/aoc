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

def match_mas(mat: list[str],
              apos: Pos):
    return (match_diff(mat, (apos[0]-1,apos[1]-1), (1,1), 'MAS') or
        match_diff(mat, (apos[0]-1,apos[1]-1), (1,1), 'SAM')
     ) and (match_diff(mat, (apos[0]-1,apos[1]+1), (1,-1), 'MAS') or
        match_diff(mat, (apos[0]-1,apos[1]+1), (1,-1), 'SAM')) 

# this is all the locations that a search starts
all_as = list(filter(lambda p: p[1], 
                     zip((m+1 for m in range(n-2)),
                         map(lambda s: findall(s[1:-1],'A',1), mat[1:-1]))))

# initiate this on all locations
truths=[match_mas(mat, apos) 
 for apos in (
     cp for cps in (itertools.product([m[0]],m[1]) for m in all_as) 
     for cp in cps)]

print(sum([1 if m else 0 for m in truths]))
