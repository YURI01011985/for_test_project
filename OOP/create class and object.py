class AutoShop():
    MAX = 200  # это константа
    maxWeidth = 1800  # это атрибут уровня класса AutoShop

    def __init__(self, marks, model):
        self._marks = marks  # атрибут уровня экземпляра класса, защищенный
        self.__model = model  # атрибут уровня экземпляра класса, приватный


a = AutoShop('BMW', '7')
print(a._AutoShop__model)  # Обращение к приватному атрибуту
print(a._marks)
print(AutoShop.MAX)  # обращение к константе
AutoShop.MAX = 250  # изменение константы!!! по сути это не константа
print(AutoShop.MAX)
