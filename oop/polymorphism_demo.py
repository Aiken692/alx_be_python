import math

# Base Class - Shape
class Shape:
    def area(self):
        """Base method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area method.")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the rectangle's area."""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the circle's area."""
        return math.pi * (self.radius ** 2)
