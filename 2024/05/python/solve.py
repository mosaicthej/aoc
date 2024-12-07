#!/usr/bin/python

# first save rules into dict
nrules=int(input())

prevRules = dict()
postRules = dict()

for _ in range(nrules):
    before,after=map(int,input().split('|'))
    bs = prevRules.get(after)
    prevRules[after] = [before]+bs if bs else [before]

    af = postRules.get(before)  # commutative
    postRules[before] = [after]+af if af else [after] 
    # communitive order

npages=int(input())


# returns true if this page is before everything
def pageGoodAfter(p:int, afs:list[int]):
    if p==75: print(p,afs)
    return ((not afs) or # base case
            ((( (not prevRules.get(afs[0])) or # this page dont care or
                (p in prevRules.get(afs[0])) # p is good for this page
               ) and
              ( (not postRules.get(p)) or # this page dont care or
                (afs[0] in postRules.get(p)) # head of afs after curr
               )
              ) and # either ways, p is good with this page, then test others
             pageGoodAfter(p, afs[1:])))

# returns true if entire manual is good (upon each page)
def manualGood(ps:list[int]):
    return ((not ps) or # base case
            (pageGoodAfter(ps[0],ps[1:]) and
             manualGood(ps[1:])))


m = list(map(lambda s: list(map(int, s.split(','))),
       (input() for _ in range(npages)) # each manual
   ))

a = list(filter(manualGood,m))

print(sum(map(lambda l: l[len(l)//2], a)))
