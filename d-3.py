import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def diagonal(self):
        return round(math.sqrt((self.side**2) * 2), 2)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21


# rectangle1 = Rectangle(height=5, width=6)
# print(rectangle1.area())  # 30.00
# print(rectangle1.diagonal())  # 7.81

# rectangle2 = Rectangle(height=3, width=3)
# print(rectangle2.area())  # 9.00
# print(rectangle2.diagonal())  # 4.24
