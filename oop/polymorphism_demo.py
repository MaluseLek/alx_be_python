import math
class Shape:
    
    def area(self):
        raise NotImplementedError("Derived Subclasses muneed to implement the area method")
    

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    

    