#!/usr/bin/python

# first line is the n lines:
n = int(input())

# put the lines into lists:
print(
    sum(
        map(lambda x,y: abs(x-y),
            *map(sorted, 
              zip(*(map(int, 
                        input().split()) # convert to ints
                for _ in range(n))) # unzip into 2 lists
            ) # sort 2 lists
        ) # result in diff
    ) # sum
)
