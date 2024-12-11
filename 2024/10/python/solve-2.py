#!/usr/bin/python
n,m = tuple(map(int, input().split(',')))
mat = tuple(tuple(map(int, input())) for _ in range(n))

Pos = tuple[int, int]
dirs = ((-1,0),(0,1),(1,0),(0,-1))

def posadd(a:Pos, d:Pos)->Pos: return (a[0]+d[0], a[1]+d[1])
def posgood(a:Pos)->bool: return not(a[0]<0 or a[0]>=n or a[1]<0 or a[1]>=m)
def slopegood(p0:Pos, p1:Pos)->bool: 
    return mat[p0[0]][p0[1]]+1==mat[p1[0]][p1[1]]
def posneigh(a:Pos)->tuple[Pos]: 
    return tuple(filter(posgood,
                        (posadd(a,d) for d in dirs)))

trailheads = tuple((r,c) for r in range(n) for c in range(m) if (not mat[r][c]))

def walkTrail(start:Pos, iheight:int)->int:
    ''' walk a trail and return the scores
    start: current location,
    iheight: current height,
    
    return 0 the score of this path'''
    print(start, iheight)
    if iheight == 9: return 1
    nextsteps = tuple(filter(
        lambda p: slopegood(start,p), posneigh(start)))
    if not nextsteps: return 0
    return sum((walkTrail(p, iheight+1) for p in nextsteps))

print(sum(walkTrail(th, 0) for th in trailheads))
