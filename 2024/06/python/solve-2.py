#!/usr/bin/python
from typing import Optional
import operator


n=int(input())
MODES = '^>v<'
'''
10
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''
type Pos=Optional[tuple[int,int]]

mat = [input() for _ in range(n)]

def findGuard(mat:list[str], r:int, g:str)->Pos:
    return (None if not mat else 
            (findGuard(mat[1:], r+1, g) if mat[0].find(g) < 0 else
             (r, mat[0].find(g)))) # base case 2: found

grot = lambda m: MODES[(MODES.find(m)+1)%4] # guard rotate
gdifs = ((-1,0), (0,1), (1,0), (0,-1)) # guard diff list
gm2d = lambda m: gdifs[MODES.find(m)] # guard mode to diff
padd = lambda p,d: tuple(map(operator.add, p, d)) # position adder

guard_currpos = findGuard(mat, 0, '^')

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


'''states to track:
    - the entire map
    - the current location of guard
    - the mode of the guard
returns the state for next step

additional states to track for part 2:
    - the trace of the guard list[(Pos, direction)]
    - whether caused a loop (yet) or not
'''
@tail_call_optimized
def nextState(mat:list[str], 
              gloc:Pos, 
              mode:str,
              trace: tuple[tuple[Pos,str]],
              hasLoop: bool) -> tuple[list[str], tuple[tuple[Pos,str]], bool]:
    gr,gc = gloc
    ntrace = trace
    if (gr < 0 or gr >= n or gc < 0 or gc >= len(mat[0])): 
        return (mat, ntrace, False) # the guard is out... no loop ofc...
    # if detected a loop, return
    if tuple((gloc, mode)) in trace:
        return (mat, ntrace, True)
    else: ntrace += (tuple((gloc, mode)),) # new trace list

    rmat, nmod = mat, mode
    nr,nc = padd(gloc, gm2d(mode)) # new loc for guard
    if not (nr >= 0 and nr < n and nc >= 0 and nc < len(mat[0])): # walked out
        rmat[gr] = mat[gr][:gc] + 'X' + mat[gr][gc+1:] # mark the current
        return (rmat, ntrace, False) # return the map, the guard is about to walk out
    if rmat[nr][nc]=='#': # got obstruction
        nr, nc = gloc # reset location
        nmod = grot(mode)
    # change the current tile to x
    rmat[gr] = mat[gr][:gc] + 'X' + mat[gr][gc+1:]
    # set the guard to new loc
    if (nr >= 0 and nr < n and nc >= 0 and nc < len(mat[0])):
        rmat[nr] = mat[nr][:nc] + nmod + mat[nr][nc+1:]
    # done update, call next move
    return nextState(rmat, (nr,nc), nmod, ntrace, hasLoop)

fst = nextState(mat, guard_currpos, '^', tuple(), False)

print(sum(map(lambda x: x.count('X'), fst[0])))

path = (p[0] for p in fst[1][1:])

universe = [
        mat[:stn[0]] +
        [mat[stn[0]][:stn[1]] + '#' + mat[stn[0]][stn[1]+1:]] +
        mat[stn[0]+1:] for stn in path
    ]
runs = (nextState(u
