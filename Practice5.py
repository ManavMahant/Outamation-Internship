# Concept of private and public

"""
class Account:
    def __init__(self, acc_num, __acc_pass):
        self.acc_num = acc_num
        self.acc_pass = __acc_pass


acc1 = Account("12345", "asdfg")
print(acc1.acc_num)
print(acc1.__acc_pass)"""


# Inheritance

"""
class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stoped...")

class Fordcar(Car):
    def __init__(self, name):
        self.name = name

car1 = Fordcar("F150-Raptor")
car2 = Fordcar("Mustang")

print(car1.start())
print(car2.color)"""


"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Manav", "Mahant", 2021)
x.welcome()

x1 = Student("Jay", "Patel", 2021)
x1.welcome()"""


# Polymorphism
"""
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def move(self):
        print("Drive")

class Boat(Vehicle):
    def move(self):
        print("Sail")

class Plane(Vehicle):
      def move(self):
        print("Fly")

    
car1 = Car("Ford", "Mustang")       
boat1 = Boat("Lamborghini", "Tecnomar") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  print("Brand : ",x.brand)
  print("Model : ",x.model)
  x.move()
"""
