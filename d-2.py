import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def diagonal(self):
        return round(math.sqrt(self.width**2 + self.height**2), 2)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24

# # 半径1の円
# circle1 = Circle(radius=1)
# print(round(circle1.area(), 2))  # 3.14
# print(round(circle1.perimeter(), 2))  # 6.28

# # 半径3の円
# circle3 = Circle(radius=3)
# print(round(circle3.area(), 2))  # 28.27
# print(round(circle3.perimeter(), 2))  # 18.85
