#!/usr/bin/python

import operator
from itertools import chain


R,C = tuple((int(x) for x in input().split(' ')))

MAT = tuple(input() for _ in range(R))
fresh = [[True for _ in range(C)] for _ in range(R)]

Pos = tuple[int, int]
Side = tuple[Pos,Pos] # when add side by each pos, always do: self, neighbour
dirs = ((-1,0),(0,1),(1,0),(0,-1))
padd = lambda p, d: tuple(map(operator.add, p, d))
get_neighs = lambda p: map(lambda d: padd(p,d), dirs)
get_sides = lambda p: zip((p,p,p,p), get_neighs(p))
get_clr = lambda p: MAT[p[0]][p[1]]
side_alt = lambda s: (s[1],s[0])
# return 4 sides of a pos, those 4 sides are within a map
pos_good = lambda p: p[0]>=0 and p[0]<R and p[1]>=0 and p[1]<C
# determine if a position is a valid square.
# note, we CAN use bad squares for describing sides.
pos_match_tmp = lambda s: lambda p: MAT[p[0]][p[1]]==s 
# find if a pos has the matching color as the given
sum_a = 0
def calc_region(p:Pos, sym:str, sides:list[tuple[Pos,Pos]]) -> None:
    '''
    p:      the current position of this square
    sym:    symbol of this current search
    sides:  sides that has been included so far, 
            *** this is SHARED and MUTABLE ***
            a side is defined as:
            A single square, will by default, put 4 sides in the list.
            for each NEW square in the region (if the square is fresh),
            it will add 4 other sides, but, if any sides already exists in the
            list, remove it.
            In the end, (POS,POS) which represents a side will be in this list
            iff it's *active* side in this region.
            because the tuple type is NOT agnostic to the ordering, when 
            checking for the existence of (S0,S1), need to check (S1,S0) as well
    return: total area of this region
    
    THIS IS SO FUNCTIONALLY IMPURE IT SHOULD BE A CRIME LOL
    '''
    def add_side(s: Side, ss: list[Side])->None:
        if s in ss: ss.remove(s)
        elif (s[1],s[0]) in ss: ss.remove((s[1],s[0]))
        else:
            # ss.append(tuple(sorted(s)))
            ss.append(s)
            return

    pos_match = pos_match_tmp(sym) # build, now pos_match is a func takes 1 para
    pos_interest = (lambda p: 
                    pos_good(p) and fresh[p[0]][p[1]] and pos_match(p))
    # takes a lot to be considered....

    if not (fresh[p[0]][p[1]] and
            MAT[p[0]][p[1]]==sym) : return # bad / repeated squre
    fresh[p[0]][p[1]] = False # mark this point as touched
    # print("touches ", p)
    global sum_a, areas
    areas.append(p)
    sum_a += 1
    nss = get_sides(p) # nss are the 4 sides that is 
    nes = filter(pos_interest, get_neighs(p)) # nes has nextstep neighbours

    [_ for _ in map(lambda s: add_side(s, sides), nss)] # add all sides
    nex = next(nes, None)
    if not nex: return  # no good neighbours, base case
    else: # return sum([calc_region(np, sym, sides) for np in chain((nex,), nes)])
        for np in chain((nex,),nes):
            calc_region(np, sym, sides)

def sides2edges(ss:list[Side])->None:
   '''
   each side can have 2 orientation, H or V.
   H = {(r,c), (r+1,c)}
   V = {(r,c), (r,c+1)}

   for H: the adjacents are: ((r,c+i), (r+1, c+i)
   and for V they would be : ((r+i, c), (r+i, c+1))
   '''
   i,n = 0,len(ss)
   while i<n:
       s = ss[i]
       p0 = s[0]
       if (abs(s[0][0]-s[1][0])==1): # H
           d = -1
           sadj = ((s[0][0],s[0][1]+d),
                    (s[1][0],s[1][1]+d))
           p1 = sadj[0]; p1_a = sadj[1]
           print("trimming with type H", s)
           while ((sadj in ss or side_alt(sadj) in ss) and 
                  (get_clr(p0)==get_clr(p1))):
               if sadj in ss: ss.remove(sadj)
               else: ss.remove(side_alt(sadj))
               print("	trim on left...", sadj, end='\n')
               d -= 1 # move to left
               n -= 1 # dec on len
               p0 = sadj[0]
               sadj = ((s[0][0],s[0][1]+d),
                    (s[1][0],s[1][1]+d))              
               p1 = sadj[0]; p1_a = sadj[1]
           d = 1
           sadj = ((s[0][0],s[0][1]+d),
                    (s[1][0],s[1][1]+d))
           p1 = sadj[0]; p1_a = sadj[1]
           while ((sadj in ss or side_alt(sadj) in ss) and 
                  (get_clr(p0)==get_clr(p1))):
               if sadj in ss: ss.remove(sadj)
               else: ss.remove(side_alt(sadj))
               print("	trim on right...", sadj, end='\n')
               d += 1 # move right
               n -= 1
               p0 = sadj[0]
               sadj = ((s[0][0],s[0][1]+d),
                    (s[1][0],s[1][1]+d))              
               p1 = sadj[0]; p1_a = sadj[1]
       else: # V
           d = -1
           sadj = ((s[0][0]+d,s[0][1]),
                    (s[1][0]+d, s[1][1]))
           p1 = sadj[0]; p1_a = sadj[1]
           print("trimming with type V", s)
           while ((sadj in ss or side_alt(sadj) in ss) and 
                  (get_clr(p0)==get_clr(p1))):
               if sadj in ss: ss.remove(sadj)
               else: ss.remove(side_alt(sadj))
               print("  trim up....", sadj, end='\n')
               d -= 1 # move to up
               n -= 1 # dec on len
               p0 = sadj[0]
               sadj = ((s[0][0]+d,s[0][1]),
                   (s[1][0]+d,s[1][1]))              
               p1 = sadj[0]; p1_a = sadj[1]
           d = 1
           sadj = ((s[0][0]+d,s[0][1]),
                   (s[1][0]+d, s[1][1]))
           p1 = sadj[0]; p1_a = sadj[1]
           while ((sadj in ss or side_alt(sadj) in ss) and 
                  (get_clr(p0)==get_clr(p1))):
               if sadj in ss: ss.remove(sadj)
               else: ss.remove(side_alt(sadj))
               print("  trim down...", sadj, end='\n')
               d += 1 # move to down
               n -= 1 # dec on len
               p0 = sadj[0]
               sadj = ((s[0][0]+d,s[0][1]),
                   (s[1][0]+d,s[1][1]))
               p1 = sadj[0]; p1_a = sadj[1]
       i+=1
   return

costs = 0
for r in range(R):
    for c in range(C):
        if fresh[r][c]: # only do stuff on valid r and c
            perims = []
            areas = [] # used to eliminate edges
            calc_region((r,c), MAT[r][c], perims)
            area = sum_a
            sum_a = 0
            print("shape is", MAT[r][c])
            print(perims)
            sides2edges(perims) # leave per edge only
            print("after removal")
            print(perims)
            print("perm is", len(perims), "area is", area)
            costs += len(perims) * area
            
            
print("DONE")
print(costs)
