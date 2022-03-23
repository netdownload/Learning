class Rectangle:
    
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
        
class Point:
        
    def __init__(self, x, y):
        self.x = x
        self.y = y        
           
    def distance_from_point(self, point):
        dist = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return dist
        
point1 = Point(2, 3)
point2 = Point(15, 10)

rectangle = Rectangle(Point(0, 0), Point(15, 10))
rectangle2 = Rectangle(point1, point2)
print(point1.falls_in_rectangle(rectangle))
