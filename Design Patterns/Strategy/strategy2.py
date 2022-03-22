class SomeAbstraction:
    pass

class Mixin1:
    def something(self):
        print('Mixin1')

class Mixin2:
    def something(self):
        print('Mixin2')
    
class Concrete1(SomeAbstraction, Mixin1):
    pass

class Concrete2(SomeAbstraction, Mixin2):
    pass


duck1 = Concrete1()
duck1.something()