add5=lambda x:x+5
print(add5(10))

mul= lambda x,y:x*y
print(mul(2,3))

points=[(1,2),(15,1),(5,-1),(10,4)]
print(sorted(points,key=lambda x:x[0]+x[1]))

# map
a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

# list comprehension
d= [i*3  for i in a]
print(d)

# filter
a=[1,2,3,4,5]
b=filter(lambda x:x%2==0,a)
print(list(b))

c=[x for x in a if x%2==0]
print(c)

