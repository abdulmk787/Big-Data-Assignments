#!/usr/bin/env python3

from operator import itemgetter
import sys

key = 0
dic={}

for line in sys.stdin:
	
	line = line.strip()
	key, count = line.split('\t', 1)
	try:
		key=int(key)
		count = int(count)
	except ValueError:
		continue
	if key in dic.keys():
		dic[key] += 1
	else:
		dic[key]=1
for i in sorted(dic.keys()):
	print('%s\t%s'%(i,dic[i]))
