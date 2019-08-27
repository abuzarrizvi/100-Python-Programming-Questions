import math
c=50
h=30
value = []
inpu = "100,150,180"
#items=[x for x in input().split(',')]
items=[x for x in inpu.split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))