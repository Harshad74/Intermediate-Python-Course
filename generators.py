def mygenerator():
    yield 1
    yield 2
    yield 3

g=mygenerator()
print(g)

value=next(g)
print(value)

value=next(g)
print(value)

value=next(g)
print(value)

print(sum(g))
print(sorted(g))


def countdown(num):
    print('starting')
    while num>0:
        yield num
        num-=1

c=countdown(3)

for i in c:
    print(i)


import sys

def firstn(n):
    nums=[]
    num=1
    while num<=n:
        nums.append(num)
        num+=1
    return nums
print(sum(firstn(10)))

def mygenerator(n):
    num=1
    while num<=n:
        yield num
        num+=1

print(sum(mygenerator(10)))
print(sys.getsizeof(firstn))
print(sys.getsizeof(mygenerator))


def fibonacci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

fib=fibonacci(30)
for i in fib:
    print(i)

mygenerator=(i for i in range(10) if i%2==0)
print(list(mygenerator))