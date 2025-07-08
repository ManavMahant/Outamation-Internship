#File I/O , OOP 

"""f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()"""

"""f = open("demo.txt","w")
f.write("I am doing internship in outamation.")
f.close()"""
"""
f = open("demo.txt", "a")
f.write("\nAnd I will learn Python\nthen MySQL and Power BI in next three months.")
f.close()"""

"""
day = int(input("Enter match day = "))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
"""
"""
with open("sample.txt", "w") as f:
    f.write("Hi everyone\nWe are learning file I/O\nusing Java\nI like programing in Java.")
    """
"""
with open("sample.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    
with open("sample.txt", "w") as f:
    f.write(new_data) """
"""
word = input("Enter a word = ")
with open("sample.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found")
        """
"""
def check_for_word():
    word = input("Enter a word = ")
with open("sample.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found")"""

"""class Student:
    name = "Manav"
    age  = 22
    
s1 = Student()
print(s1.name)
print(s1.age)
"""
"""
class Car:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

c1 = Car("Ford", "Black", 1967)
print(c1.name, c1.color, c1.year)

c2 = Car("BMW", "Blue", 1985)
print(c2.name, c2.color, c2.year)"""


class Account:
    def __init__(self,name,bal,acc):
        self.name = name
        self.balance = bal
        self.account = acc

def debit( self, amount ):
    self.balance =- amount
    print("RS", amount, "was debited")

def credit( self, amount ):
    self.balance += amount
    print("Rs", amount, "was credited")

def get_balance(self):
    return self.balance

acc1 = ("Manav", 100000, 990000001)
print(acc1.name)
print(acc1.balance)
print(acc1.account)