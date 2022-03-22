class Person:
    
    def __init__(self, n, a):
        self.name = n
        self.age = a


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
          
          
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False
           
           
    def distance_from_point(self, point):
        dist = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return dist
    

        
person1 = Person('John', 25)
print(person1.name)
        



point1 = Point(10, 20)
point2 = Point(5, 15)

print(point1.falls_in_rectangle((2, 2), (25, 25)))
print(point1.distance_from_point(point2))


        