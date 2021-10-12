#!/usr/bin/env python3
import sys
total_contrib=0
curr_node=-1
for line in sys.stdin:
    line=line.strip()
    dest,src,contrib=line.split(',')
    try:
        dest=int(dest)
        src=int(src)
        contrib=float(contrib)
    except ValueError:
        continue
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

print(curr_node,round(0.15+0.85*(total_contrib),2),sep=',')    
    