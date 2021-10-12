#!/usr/bin/env python3

import sys
import json
import math

v=sys.argv[1]
embed=sys.argv[2]
v=open(v,'r')
embed=open(embed,'r')
embed=json.load(embed)
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

for line in sys.stdin:
    line=line.strip()
    src,dests=line.split('-')
    dests=dests.split(',')
    contr=list(map(lambda x:round(1/len(dests),2),dests))
    #print(contr)
    sim_mat=list(map(lambda x:round(similiarity(src,x),2),dests))
    #print(sim_mat)
    final_contrib=[contr[i]*sim_mat[i] for i in range (len(contr))]
    for i in range(len(dests)):
        print(dests[i],src,final_contrib[i],sep=',')