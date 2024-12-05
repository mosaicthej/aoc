#!/usr/bin/python
from functools import reduce

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

