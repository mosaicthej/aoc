#!/usr/bin/python
from functools import reduce
from itertools import combinations

def is_strictly_increasing(lst):
    if not lst:  # Handle empty list case
        return False
    return reduce(lambda acc, x: 
                    acc and 
                    (x[0] < x[1]) and 
                    (x[1]-x[0] <= 3), 
                  zip(lst, lst[1:]), True)

def is_strictly_decreasing(lst):
    if not lst:  # Handle empty list case
        return False
    return reduce(lambda acc, x: 
                      acc and 
                      (x[0] > x[1]) and 
                      (x[0]-x[1] <=3 ), 
                  zip(lst, lst[1:]), True)

n=int(input())

c=0
for _ in range(n):
    l = list(map(int, input().split()))
    if (is_strictly_decreasing(l) or 
        is_strictly_increasing(l) or
        reduce(lambda acc, x: acc or x,
               map( lambda l:
                        is_strictly_increasing(l) or
                        is_strictly_decreasing(l),
                   combinations(l, len(l)-1)
                   )
               )
        ):
        c+=1

print(c)


