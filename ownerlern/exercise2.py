from math import sqrt


class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f"Shape:\n- middle: x = {self.x}, y = {self.y}\n- color: {self.color}")

    # def distance(self, x2, y2):
    def distance(self, shape):
        x2 = shape.x
        y2 = shape.y
        c = (self.x - x2) ** 2 + (self.y - y2) ** 2
        result = sqrt(c)
        return result

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie {self.x}, {self.y}"


shape1 = Shape(0, 0, "red")
shape1.describe()
shape2 = Shape(10, 10, "blue")
# print(shape1.distance(shape2.x, shape2.y))
print(shape1.distance(shape2))
print(shape1)