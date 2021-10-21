v=open('/home/pes1ug19cs007/BD/A2/v','r')
d=dict()
for line in v.readlines():
    line=line.strip()
    s,r=line.split(',')
    d[s]=r
sd=d.copy()
new_dict = {key:val for key, val in sd.items() if key != '5'}
print(new_dict)