import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
        
    def set_name(self, newname=""):
        self.name = newname
        
    def __str__(self):
        return "animal: " + str(self.name) + ": " + str(self.age)
        

class Cat(Animal):
    def speak(self):
        print("Meow!")
    
    def __str__(self):
        return "cat: " + str(self.name) + ": " + str(self.age)        
    
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    
    def get_friends(self):
        return self.friends
    
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    
    def speak(self):
        print("Hello!")
    
    def age_diff(self, other):
        diff = abs(self.age - other.age)
        return str(diff) + " years difference"
    
    def __str__(self):
        return "Person: " + str(self.name) + ": " + str(self.age)  
    
    
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    
    def change_major(self, major):
        self.major = major
        
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif r >= 0.25 and r < 0.5:
            print("I need a sleep")
        elif r >= 0.5 and r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")

    def __str__(self):
        return "Student: " + str(self.name) + ": " + str(self.age) + ": " + str(self.major)
    
    
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)
    
    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2
    
    def __add__(self, other):
        return Rabbit(0, self, other)
    
    def __str__(self):
        return "rabbit: " + str(self.rid).zfill(3)
    
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite    
    
myanimal = Animal(3)
print(myanimal.age)
myanimal.name = "Kiri"
print(myanimal.name)
myanimal.set_name("Tobby")
print(myanimal.get_age())
print(myanimal.get_name())
print(myanimal)

kiry = Cat(3)
print(kiry.get_age())
kiry.set_name("Kiry")
print(kiry.get_name())
kiry.speak()
print(kiry)

tom = Person("Tom", 35)
alice = Person("Alice", 25)
alice.add_friend("Tom")
alice.add_friend("Bob")
print(alice.get_friends())
alice.speak()
print(alice)
print(alice.age_diff(tom))

katty = Student("Katty", 25)
katty.speak()
katty.change_major(0.7)
print(katty.major)
print(katty)


rabbit1 = Rabbit(3, "bob", "mary")
rabbit2 = Rabbit(5)

print(rabbit1.get_rid())
print(rabbit2.get_rid())
print(rabbit1.get_parent1())

rabbit3 = rabbit1 + rabbit2
rabbit4 = rabbit1 + rabbit2
rabbit5 = rabbit2 + rabbit1
print("rabbit3", rabbit3.get_rid())
print(rabbit3.get_parent1())
print(rabbit3.get_parent2())

print(rabbit5 == rabbit4)