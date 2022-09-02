x=5
if x<0:
    raise Exception('x should be positive')

x=1
assert(x>=0),'x should be positive'

try:
    a=5/1
    b=a+1
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('done')



# self defined exception
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def _init_(self, message, value):
        self.message=message
        self.value=value


def value_test(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallError('value is too small',x)

try:
    value_test(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)
