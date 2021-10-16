#!/usr/bin/env python3
import sys



total_contrib=0

dic=dict()
sd=dict()
for line in sys.stdin:
    line=line.strip()
    src,dest,contrib=line.split(' ')
    try:
        dest=int(dest)
        src=int(src)
        contrib=float(contrib)
    except ValueError:
        print(src,dest,contrib,'ERROR')
        break
    if src not in dic.keys():
        dic[src]=0.15
    if dest in sd.keys():
        sd[dest]+=0.85*contrib
    else:
        sd[dest]=0.85*contrib

for i in dic.keys():
    if i in sd.keys():
        dic[i]+=sd[i]
for i in dic.keys():
    print('%d, %.2f'%(i,dic[i]))





"""         
for i in sorted(dic.keys()):
    print(i,round(dic[i],2),sep=',')

 """
""" 
    if curr_node!=dest:
        if curr_node!=-1:
            rank=0.15+0.85*(total_contrib)
            print(curr_node,round(rank,2),sep=',')
            curr_node=dest
            total_contrib=contrib
        else:
            curr_node=dest
            total_contrib=contrib
    else:
        total_contrib+=contrib
 """

    