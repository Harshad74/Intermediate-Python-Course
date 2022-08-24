tuple1=('max',25,'max')
print(tuple1)

tuple2='max','30','boston'
print(type(tuple2))

tuple3=('max',)
print(type(tuple3))

# creating a tuple from list
tuple4=tuple(['max',30,'boston'])
print(tuple4)

if 'max' in tuple1:
    print('yes')
else:
    print('no')


for i in tuple1:
    print(i)

print(tuple1.count('max'))
print(tuple1.index('max'))

a=(1,2,3,4,5,6,7,8)
b=a[::-1]
print(a[::3])
print(b)

# unpacking tuple
tuple5=(0,1,2,3,4)
i1,*i2,i3=tuple5
print(i1)
print(i3)
print(i2)


# size of tuple and list
import sys
list= [0,1,2,'hello',True]
tuple6=(0,1,2,'hello',True)
print(sys.getsizeof(list),'bytes')
print(sys.getsizeof(tuple6),'bytes')



import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=100))


