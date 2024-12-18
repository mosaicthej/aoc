from math import log10
from functools import cache

ns = (int(i) for i in input().split(" "))

ndig = lambda x: int(log10(x))
ndsp = lambda x: (x//(10**((ndig(x)+1)/2)), x%(10**((ndig(x)+1)/2)))

@cache
def blinkn(b: int, s: int):
    #print("working on blink",b,"for stone",s)
    #print(s)
    if not b: return 1 # done
    elif s==0: return blinkn(b-1, 1)
    elif (ndig(s)%2):
        return sum(map(
            lambda pms: blinkn(pms[0],pms[1]),
            zip((b-1,b-1), ndsp(s))))
    else:
        return blinkn(b-1, s*2024)


print(sum(map(lambda p: blinkn(75,p), ns)))
