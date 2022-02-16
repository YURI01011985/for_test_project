from math import pi, pow


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return pi * pow(self.r, 2)

    def get_perimeter(self):
        return 2 * pi * self.r


c1 = Circle(1)
print("{a:1.2f}".format(a=c1.get_area()))
print("{b:1.2f}".format(b=c1.get_perimeter()))
