class Rectangle:
    
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
        
class Point:
        
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
            and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False
           
           
    def distance_from_point(self, point):
        dist = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return dist
        
point1 = Point(2, 3)
point2 = Point(15, 10)

rectangle = Rectangle(Point(0, 0), Point(15, 10))
print(point1.falls_in_rectangle(rectangle))