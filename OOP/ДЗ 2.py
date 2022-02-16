class Calculator():
    @staticmethod
    def add(a, b):
        return int(a) + int(b)

    @staticmethod
    def subtract(a, b):
        return int(a) - int(b)

    @staticmethod
    def multiply(a, b):
        return int(a) * int(b)

    @staticmethod
    def divide(a, b):
        return int(a) / int(b)


# Если метод статический, то к нему можно обращаться без создания объекта!!
print(Calculator.add(1, 3))
print(Calculator.subtract(1, 3))
print(Calculator.multiply(3, 3))
print(Calculator.divide(10, 2))
# Можно также через объект
a = Calculator()
print(a.add(1, 3))
print(a.subtract(1, 3))
print(a.multiply(3, 3))
print(a.divide(10, 2))
