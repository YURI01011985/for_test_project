class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    # Статический метод @classmethod в этом случае использован как конструктор объекта
    # from_string возвращает в конструктор класса Employee
    # аргументы (first_name, last_name, int(salary)
    @classmethod
    def from_string(cls, mystring):
        list1 = mystring.split('-')
        first_name = list1[0]
        last_name = list1[1]
        salary = list1[2]
        return cls(first_name, last_name, int(salary))


a = Employee('1', '2', '3')
print(a.first_name)
print(a.last_name)
print(a.salary)

a1 = Employee.from_string('10-20-30')
print(a1.first_name)
print(a1.last_name)
print(a1.salary)
