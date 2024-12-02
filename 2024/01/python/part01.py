#!/usr/bin/python

# first line is the n lines:
n = int(input())

# put the lines into lists:
print( sum(
        map(lambda x,y: abs(x-y),
            *map(sorted, 
              zip(*(map(int, 
                        input().split()) 
                    for _ in range(n)))))
              )       
      )
