#!/usr/bin/python


from collections.abc import Generator
from typing import Optional
import itertools
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



def is_compact(s:str) -> bool:
    '''
    determine if the disk is compact
    if compact, all free block is by the end.
    '''
    n = len(s)
    f0 = s.find('.') # first free block
    return s[f0:]=='.'*(n-f0)

Fblk = tuple[int, int] # (fd, blks)

def take_nblocks(ns: tuple[Fblk], accu: tuple[Fblk], blk:int
                 ) -> tuple[tuple[Fblk], tuple[Fblk]]:
    '''
    @param: 
        ns: seq of (fd, blks)s;
        accu: accum, files taken out so far
        blk: n blk to defrag
    @return: 
        -> result list with n blk of files taken out, 
        -> files taken out
    '''
    nns = [f for f in ns if f[1]] # use on next call, also removes empty files
    if blk==0:return (ns, accu) # base case
    if not(nns): return (ns, accu)
    last_file = nns[-1] # file on the end of the list
    blk_mov = min(blk, last_file[1]) # at most move an entire file
    nns[-1] = (last_file[0], last_file[1]-blk_mov) # remove b blk away...
    to_move = (last_file[0], blk_mov) # those blks to be moved
    # the accumulator will be ordered: new fd -> old fd
    if not accu: naccu = (to_move,)
    elif last_file[0] == accu[0][0]: # same file
        naccu = ((accu[0][0], accu[0][1]+blk_mov),)+accu[1:]
    else: naccu = accu + (to_move,) # prepend
    return take_nblocks(tuple(nns), naccu, blk-blk_mov)

@tail_call_optimized
def defrag(s:tuple[Fblk], r:tuple[Fblk], 
           fblks:Generator[int,None,None], nn:int) -> tuple[Fblk]:
    '''
    move files n at a time, where n_i is the current block of free things we have
    r: seq of memory *so far* (i.e., until the first free block)
    s: seq of the memory to be examined....

    Example: '12345':
        - s = ((1,3), (2,5)) # n of (fd, size)
        - r = ((0,1),) # fd=0, size=1; this is our accu, and to be returned.
        - fblks would yield: 2,4
    '''
    # if no free block left, then defrag is done....
    if nn is None or not s: return r # r is the result str
    ns, nrr = take_nblocks(s, tuple(), nn) # rest of mem, addition to build to r
    nnn = next(fblks, None)
    nr =  r + nrr + (ns[0],) if not nnn is None else r+ns+nrr # building....
    return defrag(ns[1:], nr, fblks, nnn) # recurse

s0 = input() # input
free_blks = (int(s0[i]) for i in range(len(s0)) if i%2)
f0 = next(free_blks,None)
file_blks = ((i//2, int(s0[i]),) for i in range(len(s0)) if (not i%2))

defragged = (next(file_blks),)
defragged = defrag(tuple(file_blks), defragged, free_blks, f0)

print(defragged)
# defragged is the tuple of ((fd, size))

arith_sum = lambda x0,xn,n:(x0+xn)*n/2
# given a partial frag: (fd, size) and current blk, 
# return the parital checksum: ex: (4,3),9: 4*(9+10+11)
partial_sum = lambda frag,bn: frag[0] * arith_sum(bn,bn+frag[1]-1,frag[1])

sizes = (size for (_,size) in defragged)
start_inds = itertools.accumulate(sizes, initial=0)
cksm_ids = zip(defragged, start_inds)

print(sum(map(lambda p: partial_sum(p[0],p[1]), cksm_ids)))
