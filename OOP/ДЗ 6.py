prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
          "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
          "Pineapple": 3.5}


class Beverage():

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = 0
        self.str2 = ''

    def get_cost(self):
        for self.now in self.ingredients:
            if self.now in prices:
                self.cost += prices[self.now]
        return "$" + "{x:1.2f}".format(x=self.cost)

    def get_price(self):
        return "$" + "{x:1.2f}".format(x=self.cost * 2.5)

    def get_name(self):
        ingredients1 = []
        str1 = ''
        for i in range(len(self.ingredients)):
            if self.ingredients[i].endswith('berries'):
                a = self.ingredients[i].strip('ies')
                b = a + 'y'
                ingredients1.append(b)
            else:
                ingredients1.append(self.ingredients[i])
        ingredients1.sort()
        if len(ingredients1) > 1:
            ingredients1.append('Fusion')
        else:
            ingredients1.append('Smoothie')
        for i in range(len(ingredients1)):
            str1 = str1 + ' ' + ingredients1[i]
        self.str2 = str1.strip()
        return self.str2


s1 = Beverage(['Raspberries', 'Strawberries', 'Blueberries'])
print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())
