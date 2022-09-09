org=5
cpy=org
cpy=6
print(cpy)
print(org)


org=[1,2,3]
cpy=org
cpy[0]=-10
print(cpy)
print(org)


import copy
org=[1,2,3]
cpy=copy.copy(org)
cpy[0]=-10
print(cpy)
print(org)



import copy
org=[[1,2,3,4],[5,6,7,8]]
cpy=copy.copy(org)
cpy[0][1]=-10
print(cpy)
print(org)


import copy
org=[[1,2,3,4],[5,6,7,8]]
cpy=copy.deepcopy(org)
cpy[0][1]=-10
print(cpy)
print(org)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Company:
    def __init__(self,boss,employee):
        self.boss=boss
        self.employee=employee


p1=Person('Alex',27)
p2=copy.copy(p1)

p2.age=30
print(p2.age)
print(p1.age)

p1=Person('Alex',55)
p2=Person('Joe',27)

company=Company(p1,p2)
company_clone=copy.deepcopy(company)
company_clone.boss.age=60
print(company_clone.boss.age)
print(company.boss.age)

