from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s- self.side_c)) ** 0.5
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    
    
        
# Creating instances of Rectangle and the Circle classes.
rectangle = Rectangle(5, 4)
circle = Circle(3)
triangle = Triangle(3, 4, 5)

# Calculating area and perimiter using the abstract method
print("Rectangle - Area:", rectangle.area(), " Perimeter:", rectangle.perimeter())
print("Circle - Area:", circle.area(), " Perimeter:", circle.perimeter())
print("Triangle - Area:", triangle.area(), " Perimeter:", triangle.perimeter())


        
        
        
        