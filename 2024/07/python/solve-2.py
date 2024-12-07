#!/usr/bin/python

import itertools, operator

n=int(input())

s=0

def expbuild(exps, accu):
    return (exps if not accu else expbuild(exps[1:], accu+exps.jon))

def leftjoin(e1:str, e2:str) -> str: # '22+', '32*'; '(22+32)+', '67+'
    return ('(' +
            e1 + 
            (e2[:-1] if e2[-1] in '+*' else e2 )+
            ')' +
            (e2[-1] if e2[-1] in '+*' else ''))

for _ in range(n):
    exps = []
    r,ex = input().split(': ')
    r,nus =int(r), ex.split(' ')
    oss = itertools.product('+*|',repeat=len(nus)-1)
    
    # exps=[''.join(tuple( map(lambda x: operator.add(x[0],x[1]) if x[1] else x[0],
      #          itertools.zip_longest(nus, os))
       #     )) for os in oss]

    for os in oss:
        build = ''
        exp = tuple( map(lambda x: operator.add(x[0],x[1]) if x[1] else x[0],
                itertools.zip_longest(nus, os))) # ('3+', '5*', '66|', '5')
        
        expl = [];i=0
        while(i<len(exp)):
            if i<len(exp) and len(expl)>0 and expl[-1][-1]=='|':
                # if the building list ends with |
                expl[-1] = expl[-1][:-1] + exp[i]
                i += 1 # exp[i] would be next
            else:
                e = exp[i] # on ith thing
                expl.append(e)
                i+=1

        print(exp,expl)
        for es in expl:
            build = leftjoin(build, es)

        res = eval(build)
        if res==r:
           s+=res
           print('happy')
           break
print(s)


