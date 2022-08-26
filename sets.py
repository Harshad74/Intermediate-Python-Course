set1={1,2,3,1,2}
print(set1)

set2=set([1,2,3])
print(set2)

set3=set("hello")
print(set3)

set4=set()
set4.add(1)
set4.add(2)
set4.add(3)

print(set4.pop())
print(set4)


odd={1,3,5,7,9}
even={0,2,4,6,8}
prime={2,3,5,7}

# union of two sets
a=odd.union(even)
print(a)

# Intersection of two sets
b=odd.intersection(prime)
print(b)

# difference of two sets
set5={1,2,3,4,5,6,7,8,9}
set6={1,2,3,10,11,12}
diff=set5.difference(set6)
print(diff)

# symmetric difference of two sets
print(set5.symmetric_difference(set6))

set5.update(set6)
print(set5)

print(set5.isdisjoint(set6))

# frozenset
c=frozenset([1,2,3,4])
print(c)