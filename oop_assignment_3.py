#Assignment – Shape Drawing Program (Polymorphism & Abstraction)
#Objective: Practice Polymorphism and Abstraction by designing a shape-drawing application.

#Instructions:

#1. Create an abstract class Shape with:

#An abstract method area()

#An abstract method perimeter()

#2. Create subclasses:

#Rectangle (with attributes: length, width)

#Circle (with attribute: radius)

#Triangle (with attributes: base, height, side lengths)

#Implement the abstract methods in each subclass.
#3. Write a function that takes a list of different shapes and prints:

#Shape type

#Area

#Perimeter

#4. Test it by creating a list with at least 5 shapes of different types.

#Expected Skills Practiced:

#Abstract classes and methods (Abstraction)

#Method overriding (Polymorphism)

#Unified handling of different objects through a common interface

from abc import ABC, abstractmethod
import math

# 1. Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 2. Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# 2. Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 2. Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# 3. Function to display shape info
def print_shape_info(shapes):
    for shape in shapes:
        print("Shape type:", type(shape).__name__)
        print("Area:", round(shape.area(), 2))
        print("Perimeter:", round(shape.perimeter(), 2))
        print("-" * 30)

# 4. Create a list of 5 shapes and test
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(6, 4, 5, 5, 6),
    Rectangle(3, 8),
    Circle(2.5)
]

print_shape_info(shapes)