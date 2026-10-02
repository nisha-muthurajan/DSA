import math
from abc import ABC,abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass
  @abstractmethod
  def perimeter(self):
    pass

class Rectangle(Shape):
  def __init__(self,l,b):
    self.l = l
    self.b = b
  def area(self):
    return self.l*self.b
  def perimeter(self):
    return 2*(self.l + self.b)
class Square(Shape):
  def __init__(self,a):
    self.a = a
  def area(self):
    return self.a**2
  def perimeter(self):
    return 4*self.a
class Triangle(Shape):
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
  def perimeter(self):
    return self.a + self.b + self.c
  def area(self):
    return 0.5 * self.b * self.c
class Circle(Shape):
  def __init__(self,r):
    self.r = r
  def area(self):
    return math.pi * self.r * self.r
  def perimeter(self):
    return 2 * math.pi * self.r


if __name__ == "__main__":
  shapes=[
    Rectangle(l=3,b=4),
    Square(a=4),
    Triangle(a=2,b=3,c=4),
    Circle(r=3)
  ]

  for i in shapes:
    print(f"{i.__class__.__name__} Area: {i.area():.2f}")
    print(f"{i.__class__.__name__} Perimeter: {i.perimeter():.2f}")
    
    
    

'''Rectangle Area: 12.00
Rectangle Perimeter: 14.00
Square Area: 16.00
Square Perimeter: 16.00
Triangle Area: 6.00
Triangle Perimeter: 9.00
Circle Area: 28.27
Circle Perimeter: 18.85
'''    