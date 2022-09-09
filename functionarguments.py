def fun(a,b,c,d=4):
    print(a,b,c,d)

fun(1,2,3)


def fun1(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

fun1(1,2,3,4,5,six=6,seven=7)


def fun2(a,b,*,c,d):
    print(a,b,c,d)

fun2(1,2,c=3,d=4)


def fun3(*args,last):
    
    for arg in args:
        print(arg)
    print(last)

fun3(1,2,3,last=4)


def fun3(a,b,c):
    print(a,b,c)

mylist=[1,2,3]
fun3(*mylist)


def fun4(a,b,c):
    print(a,b,c)

mydict={'a':1,'b':2,'c':3}
fun4(**mydict)


def fun5():
    global number
    x=number
    number=3
    print('number inside function:',x)

number=0
fun5()
print(number)



def fun6(a_list):
    a_list=a_list+[200,300,400]

mylist=[1,2,3]
fun6(mylist)
print(mylist)



def fun6(a_list):
    a_list+=[200,300,400]

mylist=[1,2,3]
fun6(mylist)
print(mylist)