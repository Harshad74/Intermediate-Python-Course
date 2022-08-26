from timeit import default_timer as timer
string1='I\'m a programmer'
print(string1)

string2='''Hello
world'''
print(string2)

string3='Hello world'
substring=string3[1:7]
print(substring)

# reversing a string
substring=string3[::-1]
print(substring)

string4=' hello world  '
string=string4.strip()
print(string)

print(string4.startswith('hello'))
print(string4.find('lo'))

# replacing word in a string
print(string4.replace('world','universe'))

# splitting string
string5='how are you'
list=string5.split()
print(list)

# making string from list
string6=' '.join(list)
print(string6)


mylist=['a']*5
print(mylist)

start=timer()
string7=''.join(mylist)
stop=timer()
print(stop-start)
print(string7)

# formatting a string
var='tom'
string8="the variable is %s" % var
print(string8)

var=3.12567
var2=7
print('the variable is {:.2f} and {}'.format(var,var2))


var=3.12567
var2=7
print(f'the variable is {var} and {var2}')



