import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self.area = math.pi * radius ** 2
        self.circumference = 2 * math.pi * radius

    def get_radius(self):
        return self._radius

    @property
    def radius(self):
        return self.get_radius()

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius
        self.area = math.pi * new_radius ** 2
        self.circumference = 2 * math.pi * new_radius


a = Circle(10)
a.radius = 30
print(a.radius)