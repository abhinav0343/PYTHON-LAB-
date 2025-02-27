import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
def main():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    rectangle = Rectangle(width, height)
    print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
main()