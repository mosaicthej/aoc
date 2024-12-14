X,Y=101,103

QS = (((0,0),            (X//2,Y//2)), # Q1
      ((X//2+1, 0),      (X, Y//2)),   # Q2
      ((X//2+1, Y//2+1), (X,Y)),       # Q3
      ((0, Y//2+1),      (X//2, Y)))   # Q4

in_quad = (lambda p,Q:
           p[0]>=Q[0][0] and p[1]>=Q[0][1] and p[0]<Q[1][0] and p[1]<Q[1][1])

TIME=100

from operator import add, mod, mul
from functools import reduce

n=int(input())

ins = tuple(( input() for _ in range(n) ))

ps,vs = zip(
    *map(lambda spp: 
        map(lambda il: # (((12,18),(11,7)),...)
            tuple(map(int,il)), 
            map(lambda sp:  # ((('12','18'), ('11','7')),...)
                sp.split(','),
                spp)),
        map(lambda l: # (('12,18', '11,7'),...)
            map(lambda pves: 
                pves.split('=')[1], 
                l), # (["12,18", "11,7"], ....
            map(lambda s: 
                s.split(' '), 
                ins)))) # (["p=12,18", "v=11,7"], ....)

def moven(ps: tuple[tuple[int,int]],
          vs: tuple[tuple[int,int]],n:int):
    if not n: return tuple(map(lambda p: tuple(map(mod, p, (X,Y))), ps))

    def move1(ps, vs):
        return tuple(((lambda pv: tuple(map(add, pv[0], pv[1])))(pv) 
                      for pv in zip(ps,vs)))
    return moven(move1(ps,vs), vs, n-1)

res = moven(ps,vs,100)

qrobts = tuple(map(lambda Q: tuple(filter(lambda rp: in_quad(rp,Q), res))
             , QS))  # 4 quardants contains robot's location

ans = reduce(mul, 
                map(lambda ps:
                    sum(map(lambda _: 1, ps)),
                    qrobts), 
                1)
print(ans)
