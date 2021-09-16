#!/usr/bin/env python3

from operator import itemgetter
import sys

dic={}
prev_state=None
prev_city=None
city_count=0
state_count=0
for line in sys.stdin:
	
	line = line.strip()
	state, city, count = line.split(',', 2)
	try:
		count = int(count)
	except ValueError:
		continue

	if prev_state==state:
		if prev_city==city:
			city_count+=count
			state_count+=count
		else:
			if prev_city:
				print(prev_city,city_count)
			prev_city=city
			city_count=count
			state_count+=count
	else:
		if prev_state:
			print(prev_city,city_count)
			print(prev_state,state_count)
			print(state)
		else:
			print(state)
		prev_city=city
		prev_state=state
		city_count=count
		state_count=count 
print(prev_city,city_count)
print(prev_state,state_count)
