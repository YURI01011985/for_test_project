from collections import namedtuple

Auto = namedtuple('Auto', 'model year color')
mytuple = Auto('a6', 2000, 'red')
print(mytuple.model)
print(mytuple.year)
print(mytuple.color)
