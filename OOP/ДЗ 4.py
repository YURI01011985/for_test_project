class Pizza():
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def garden_feast(cls):
        a = 'spinach'
        b = 'olives'
        c = 'mushroom'
        return cls([a, b, c])

    @classmethod
    def hawaiian(cls):
        a = 'ham'
        b = 'pineapple'
        return cls([a, b])

    @classmethod
    def meat_festival(cls):
        a = 'beef'
        b = 'meatball'
        c = 'bacon'
        return cls([a, b, c])


p1 = Pizza.garden_feast()
print(p1.order_number)
print(p1.ingredients)
p2 = Pizza(['ham', 'pineapple'])
print(p2.order_number)
print(p2.ingredients)
