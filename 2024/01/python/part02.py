#!/usr/bin/python

# first line is the n lines:
n = int(input())

A,B = zip(*(map(int,
          input().split()) 
      for _ in range(n))) # input into 2 lists

print(
    sum(
        map(lambda x: x*B.count(x), A)
    )
)

