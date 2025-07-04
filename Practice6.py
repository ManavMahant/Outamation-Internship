"""class Student:
    def __init__(self, phy, sci, math):
        self.phy = phy
        self.sci = sci
        self.math = math
    @property
    def percentage(self):
        return str((self.phy + self.sci + self.math) /3 ) + "%"
    

s1 = Student(75,68,80)
print(s1.percentage)

s1.sci = 86
print(s1.percentage)"""


"""class Bank:
    def __init__(self,name,bal,acc):
        self.name = name
        self.balance = bal
        self.account = acc

    def debite(self,amount):
        self.balance =- amount
        print("Rs" ,amount , "was debited from your account")

    def credit(self,amount):
        self.balance += amount
        print("Rs", amount, "was credited in Your account")

    def get_balance(self):
        return self.balance
    
    acc1 = ("Mandeep", 100000000, 9876543210)
    print(acc1.name)
    print(acc1.balance)
    print(acc1.account)"""

""
# Scope
"""
x = 300             # Global scope

def myfunc():
  x = 200           # Local scope
  print(x)

myfunc()

print(x)
"""

# Modules

"""
import mymodule
mymodule.greeting("Manav")

x = mymodule.person1["country"]
print(x)"""


"""
import datetime
x = datetime.datetime.now()
print(x)"""


"""
import datetime
x = datetime.datetime.now()
print(x.strftime("%D"))
print(x.strftime("%B"))
print(x.year)
"""

