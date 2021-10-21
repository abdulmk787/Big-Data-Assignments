#!/usr/bin/env python3
import sys
curr_node=-1
rank=0
for line in sys.stdin:
    line=line.strip()
    dest,src,contrib=line.split(' ')
    try:
        dest=int(dest)
        contrib=float(contrib)
    except ValueError:
        continue

    if curr_node!=dest:
        if curr_node!=-1:
            print('%d,%.2f'%(curr_node,rank))
            curr_node=dest
            rank=0.15+0.85*contrib
            
        else:
            curr_node=dest
            rank=0.15+0.85*contrib
    else:
        rank+=0.85*contrib

print('%d,%.2f'%(curr_node,rank))
    
#     if src not in dic.keys():
#         dic[src]=0.15
#     if dest in sd.keys():
#         sd[dest]+=0.85*contrib
#     else:
#         sd[dest]=0.85*contrib

# for i in dic.keys():
#     if i in sd.keys():
#         dic[i]+=sd[i]
# for i in dic.keys():
#     print('%d,%.2f'%(i,dic[i]))
