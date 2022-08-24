dict1=dict(name='ajay',age=28,city='pune')
print(dict1)

dict1['email']='ajay@xyz.com'
print(dict1)

del dict1['name']
print(dict1)

dict1.pop('age')
print(dict1)

dict1.popitem()
print(dict1)


# printing contents of dictionary
for key,value in dict1.items():
    print(key,value)


# copying a dictionary
dict2=dict1.copy()
dict2['name']='anuj'
print(dict2)
print(dict1)

dict1.update(dict2)
print(dict1)

mytuple=(8,7)
mydict={mytuple:15}
print(mydict)