#!/usr/bin/python

from operator import add, sub
from typing import Optional
import itertools
type Pos=Optional[tuple[int,int]]

n,m = tuple(map(int, input().split(' '))) # max row
# mat = [input() for _ in range(n)]
# all_ants = ''.join(map(lambda c: '' if c=='.' else c, ''.join(mat)))

ants_d = dict()
for r in range(n): # take inputs
    s = input()
    for c in range(m):
        if s[c]!='.':
            ps = ants_d.get(s[c])
            ants_d[s[c]] = [(r,c)] + ps if ps else [(r,c)]

# now should have a dict of positions of all antenna
ks = ants_d.keys()

posop = lambda binop: lambda p0,p1: tuple(map(binop, p0,p1))
psum = lambda p0,p1: posop(add)(p0,p1)
pdif = lambda p0,p1: posop(sub)(p0,p1)

pvalid = lambda p: ((p[0]>=0) and (p[0]<n) and
                    (p[1]>=0) and (p[1]<m)) # return if p is a valid loc
# given a pair antenna, return antinodes # d = p0 - p1;
# a0: 2x(a0-p0) = a0-p1 ; ==> a0 = p0+d
# a1: 2x(a1-p1) = a1-p0 ; ==> a1 = p1-d
get_antinodes = lambda p0,p1: (
    psum(p0, pdif(p0,p1)),
    pdif(p1, pdif(p0,p1)))

antin_ps = [[False for _ in range(m)] for _ in range(n)] # postions for antinodes

# going over each key in the dict, and for each pair of the antenna,
# find the position for antinodes
for k in ants_d:
    pps = itertools.combinations(ants_d[k],2)
    for pp in pps: # a pair of locations for antenna
        aa = get_antinodes(pp[0],pp[1])
        for a in aa: # a is a single antinode
            if pvalid(a): antin_ps[a[0]][a[1]] = True

print(sum(map(sum,antin_ps)))
