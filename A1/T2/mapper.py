#!/usr/bin/env python3

import sys
import json
import math
import requests 
 
URL = 'http://20.185.44.219:5000/'
nan='nan'
i=0
q = [float(sys.argv[1]), float(sys.argv[2])]
d= float(sys.argv[3])
for line in sys.stdin:
	line=line.strip()
	ob=json.loads(line)
	st_lat,st_lng=ob['Start_Lat'],ob['Start_Lng']
	if (str(st_lat)=='nan') or (str(st_lng)=='nan'):
		continue
	p = [st_lat, st_lng]

	if (math.dist(p,q) < d):
		data = { "latitude": st_lat, "longitude": st_lng }
		res = requests.post( url= URL, json = data)
		place = res.json()
		print('%s|%s|%s' %(place['state'], place['city'], 1) )
	