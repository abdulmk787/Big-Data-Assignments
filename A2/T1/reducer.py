#!/usr/bin/env python3
from operator import itemgetter
import sys
path=sys.argv[1]
v_file=open(path,'w')
curr_src=-1
for line in sys.stdin:
    line=line.strip()
    source,dest=line.split(' ',1)
    try:
        source=int(source)
        dest=int(dest)
    except ValueError:
        continue
    if curr_src!=source:
        if curr_src==-1:
            print('%d'%(source),end=' [')
            print('%d'%(dest),end='')
        else:
            
            print(']\n%d'%(source),end=' [')
            print('%d'%(dest),end='')
        v_file.write('%d,%d\n'%(source,1))
        curr_src=source
    elif curr_src==source:
        print(',%d'%(dest),end='')
        
print(']')