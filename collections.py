# Counter
from collections import Counter
from typing import OrderedDict
str='aaaaabbbbccc'
print(Counter(str))
print(Counter(str).most_common(1)[0][1])
print(list(Counter(str).elements()))


# namedtuple
from collections import namedtuple
a=namedtuple('point','x,y')
pt=a(1,-4)
print(pt)

# OrderedDict
from collections import OrderedDict
dict=OrderedDict()
dict['a']=1
dict['b']=2
dict['c']=3
dict['d']=4
print(dict)

# default dict
from collections import defaultdict
dict=defaultdict(int)
dict['a']=1
dict['b']=2
dict['c']=3
print(dict['d'])


# deque
from collections import deque
d=deque()
d.append(1)
d.append(2)
d.append(3)

d.pop()
d.rotate(1)
print(d)



