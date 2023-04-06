class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2  
        return (x_diff_sq + y_diff_sq)**0.5

class Fraction(object):
    '''
    Описание класса. A number representive as a fraction, Fraction (num, denom) -> (num/denom) num - числитель, 
    denom - знаменатель
    '''
    def __init__(self, num, denom):
        '''num and denom must be integer'''
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
        
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    
    def __add__(self, other):
        top = self.num*other.denom + other.num*self.denom
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
    def __sub__(self, other):
        top = self.num*other.denom - other.num*self.denom
        bott = self.num*other.denom
        return Fraction(top, bott)
    
    def __float__(self):
        return self.num/self.denom
    
c = Fraction(4, 4)
d = Fraction(4, 5)
e = Fraction(5, 6)
print(d-c)
print(float(d-c))




a = Coordinate(2, 4)
print(a)
b = Coordinate(3, 5)
print(b)
print(a.distance(b))
