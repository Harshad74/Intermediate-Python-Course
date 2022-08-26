from itertools import product

a=[1,2]
b=[3]
print(list(product(a,b)))


from itertools import permutations
a=[1,2,3]
print(list(permutations(a,2)))


from itertools import combinations, combinations_with_replacement
a=[1,2,3,4]
print(list(combinations(a,2)))
print(list(combinations_with_replacement(a,2)))

from itertools import accumulate
import operator
a=[1,2,3,4]
print(list(accumulate(a,func=operator.mul)))



from itertools import groupby

def smaller_than_3(x):
    return x<3

a=[1,2,3,4]
group_obj=groupby(a,key=smaller_than_3)
for key,value in group_obj:
    print(key,list(value))



from itertools import count,cycle,repeat

for i in count(10):
    print(i)
    if i==15:
        break

for i in repeat(1,4):
    print(i)









