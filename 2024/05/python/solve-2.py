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

class page:
    def __init__(self, a:int) -> None:
        self.p = a
    def __lt__(self, other): # self need to come before other
        return ((not prevRules.get(other.p) or  # self is before other
                 self.p in prevRules.get(other.p)) and
                (not postRules.get(self.p) or
                 other.p in postRules.get(self.p)) and
                ( (not prevRules.get(other.p)) and (not postRules.get(self.p)) and
                 (not other < self)) # check if the rule already confilcts
                ) # other is after self
    def __eq__(self, other) -> bool: return self.p==other.p
    def get_p(self): return self.p

ps2pps = lambda ps: list(map(lambda p:p.p, ps))
pps2ps = lambda pps: list(map(lambda pp:page(pp),pps))

npages=int(input())

# returns true if this page is before everything
def pageGoodAfter(p:int, afs:list[int]):
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

pss = list(map(lambda s: list(map(lambda p: page(int(p)), s.split(','))),
       (input() for _ in range(npages)) # each manual
   ))

b = list(
        filter(
            lambda ps: not manualGood(list(map(lambda p: p.p, ps)))
            , pss)) # list of bad manuals

correct = [sorted(ps) for ps in b]

print(sum((ps[len(ps)//2].get_p() for ps in correct)))
