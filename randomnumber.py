import random

a=random.random()
print(a)

b=random.uniform(1,10)
print(b)

c=random.randint(1,10)
print(c)

d=random.randrange(1,10)
print(d)

e=random.normalvariate(0,1)
print(e)

mylist=list('AWRTSDFG')
f=random.choice(mylist)
print(f)

g=random.sample(mylist,3)
print(g)

h=random.choices(mylist,k=3)
print(h)

random.seed(1)
i=random.random()
j=random.randint(1,10)
print(i,j)

random.seed(1)
k=random.random()
l=random.randint(1,10)
print(k,l)



import secrets

m=secrets.randbelow(10)
print(m)

n=secrets.randbits(4)
print(n)



import numpy as np

a=np.random.rand(3)
print(a)

b=np.random.randint(0,10,(3,3))
print(b)

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

np.random.shuffle(arr)
print(arr)

np.random.seed(1)
arr=np.random.rand(3,3)
print(arr)

np.random.seed(1)
arr=np.random.rand(3,3)
print(arr)







