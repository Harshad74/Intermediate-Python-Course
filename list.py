list1=['apple','banana','mango']
print(list1)

list2=list()
print(list2)

list3=['10',True,"mango",'mango']
print(list3)

item=list1[1]
print(item)

for i in list1:
    print(i)

if 'banana' in list1:
    print('yes')
else:
    print('no')

list1.append('cherry')
print(list1)

list1.insert(1,'lemon')
print(list1)

item=list1.pop()
print(item)

list1.remove('banana')
print(list1)

list1.reverse()
print(list1)

newlist=sorted(list1)
print(list1)
print(newlist)

list4=[1]*5
print(list4)

mylist=[1,2,3,4,5,6,7,8,9]
print(mylist[::2])

listcopy=mylist.copy()
listcopy.append(10)
print(listcopy)
print(mylist)


list=[i*i for i in mylist]
print(list)