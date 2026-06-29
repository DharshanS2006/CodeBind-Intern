class Shape:
    def area(self):
        print("Area formula depends on the shape.")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Rectangle Area:", self.length * self.breadth)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)


rectangle = Rectangle(5, 4)
circle = Circle(3)

rectangle.area()
circle.area()
