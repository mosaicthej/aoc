import sys

class TailRecurseException(Exception):  # Update to inherit from Exception
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is its own grandparent, and catching such
    exceptions to fake the tail call optimization.
    
    This function fails if the decorated
    function recurses in a non-tail context.
    """
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
                and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while True:  # Replace 1 with True for better readability
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:  # Update exception syntax
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func


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

def generate_bitmap(ps, iteration):
    bitmap = [[" " for _ in range(X)] for _ in range(Y)]
    for p in ps:
        bitmap[p[1] % Y][p[0] % X] = "."
    filename = f"txts/bitmap_{iteration:04}.txt"
    with open(filename, "w") as f:
        for row in bitmap:
            f.write("".join(row) + "\n")

@tail_call_optimized
def moven(ps: tuple[tuple[int,int]],
          vs: tuple[tuple[int,int]],n:int):
    if not n: return tuple(map(lambda p: tuple(map(mod, p, (X,Y))), ps))

    def move1(ps, vs):
        return tuple(((lambda pv: tuple(map(add, pv[0], pv[1])))(pv) 
                      for pv in zip(ps,vs)))
    generate_bitmap(ps, n)
    return moven(move1(ps,vs), vs, n-1)


res = moven(ps,vs,9999)

qrobts = tuple(map(lambda Q: tuple(filter(lambda rp: in_quad(rp,Q), res))
             , QS))  # 4 quardants contains robot's location

ans = reduce(mul, 
                map(lambda ps:
                    sum(map(lambda _: 1, ps)),
                    qrobts), 
                1)
print(ans)
