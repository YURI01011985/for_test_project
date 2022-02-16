# list1 = [1, 2, 3, 4]
# print(list1)
# list2 = list(map(lambda x: x ** 3, list1))
# print(list2)
# list3 = list(filter(lambda x: x <= 30, list2))
# print(list3)
from functools import wraps


def decor(x):
    @wraps(x)
    def y(*args):
        '''
            Подменяет основную mysum()
        '''
        print('ccc')
        x(*args)
        print('bbb')

    return y


@decor
def mysum(a, b):
    '''
    Основная
    '''
    print(a + b)


mysum(5, 10)
print(help(mysum))
