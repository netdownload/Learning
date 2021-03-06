from random import randint


class Point:
        
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
            and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
             return False
        
class Rectangle:
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def print_rectangle_coordinates(self):
        return print("Rectangle Coordinates:",
              self.point1.x, ",", self.point1.y, "and",
              self.point2.x, ",", self.point2.y)    
        
    def area(self):
        return print("Area of the rectangle =",
                     (self.point2.x - self.point1.x)*
                     (self.point2.y - self.point1.y))
        
        
rectangle = Rectangle(Point(randint(0, 9),randint(0, 9)), 
                      Point(randint(10, 19),randint(10, 19)))

rectangle.print_rectangle_coordinates()

user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

print("User point was inside rectangle: ", 
      user_point.falls_in_rectangle(rectangle))

rectangle.area()
