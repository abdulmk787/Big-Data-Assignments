#!/usr/bin/env python3

import sys
import json
path=sys.argv[1]

for line in sys.stdin:
    line=line.strip()
    from_page,to_page=line.split('\t')
    print(from_page,to_page,sep=',')
