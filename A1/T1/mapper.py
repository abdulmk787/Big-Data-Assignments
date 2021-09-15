#!/usr/bin/env python3

import sys
import json
from datetime import datetime as dt
nan='nan'
j=[]
desc=['lane blocked','shoulder blocked','overturned vehicle']
weather=['heavy snow','thunderstorm','heavy rain','heavy rain showers','blowing dust']
for line in sys.stdin:
    line=line.strip()
    ob=json.loads(line)
    res=0
    if str(ob['Description'])==nan:
        continue
    for d in desc:
        if ob['Description'].lower().find(d)!=-1:
            res=1
            break
    if res==0:
        continue
    if str(ob['Severity'])==nan or ob['Severity']<2 :
        continue
    if str(ob['Sunrise_Sunset'])==nan or ob['Sunrise_Sunset']!='Night':
        continue
    if str(ob['Visibility(mi)'])==nan or ob['Visibility(mi)']>10:
        continue
    if str(ob['Precipitation(in)'])==nan or ob['Precipitation(in)']<0.2:
        continue
    res=0
    if str(ob['Weather_Condition'])==nan:
        continue
    for w in ob['Weather_Condition'].split('and'):
        res=0
        
        if w.lower() in weather:
            res=1
            break
    if str(ob['Start_Time'])==nan:
        continue
    if res==0: 
        continue
    time=dt.strptime(ob['Start_Time'][0:19],'%Y-%m-%d %H:%M:%S')
    hr=time.hour
    print('%s\t%s'%(hr,1))
