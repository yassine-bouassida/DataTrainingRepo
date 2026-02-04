#namedtuple
from collections import *

Point = namedtuple('Point',['x','y'])
p1:Point = Point(11,22)
p2:Point = Point(33,44)

print(p1)
print(p2)

p1_dict=p1._asdict()
print(p1_dict)


######################
#defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d=defaultdict(set)
for k,v in s:
    d[k].add(v)

print(dict(d.items()))

d['purple']={6,7}

print(dict(d.items()))

print(d['green']) #returns the default value since green doesn't exist