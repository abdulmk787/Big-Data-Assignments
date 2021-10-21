#!/usr/bin/env python3

import sys
import json
import math

def similiarity(p,q):
    p=embed[p]
    q=embed[q]
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(p)):
        x = p[i]; y = q[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


pr=dict()
v=sys.argv[1]
embed=sys.argv[2]
vf=open(v,'r')

for l in vf.readlines():
    l=l.strip()
    s,r=l.split(',')
    pr[s]=r
embed=open(embed,'r')
embed=json.load(embed)
seen=pr.copy()

for line in sys.stdin:
    line=line.strip()
    src,dests=line.split(' ',1)
    dests=dests.strip('][').split(',')  #[2,3,4]
    contr=list(map(lambda x:float(pr[src])/len(dests),dests)) #[0.33,0.33,0.33]
    #print(contr)
    sim_mat=list(map(lambda x:similiarity(src,x),dests))#[0.95,0.85,0.85]
    #print(sim_mat)
    final_contrib=[contr[i]*sim_mat[i] for i in range (len(contr))]
    for i in range(len(dests)):
        print('%s %s %f'%(dests[i],src,final_contrib[i]))
        if dests[i] in seen.keys():
            seen.pop(dests[i])
for i in seen.keys():
    print('%s %s %f'%(i,'none',0.00))
    