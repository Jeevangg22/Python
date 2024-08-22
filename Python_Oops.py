"""
class Human:
    place = 'chickmagalur'

    # below are the properties of the class
    def __init__(self,name,age,company):
        self.name = name
        self.age = age
        self.company = company
        self.email = name + str(age) + '@'+company+'.com'

    # Below are the methods
    def details_info(self):
        if self.company == 'KPIT':
            print(f"{self.name} works in a {self.company} ")
        elif self.company == 'TCS':
            print(f"{self.name} works in a {self.company} ")
        elif self.company == 'WIPRO':
            print(f"{self.name} works in a {self.company} ")
        else:
            print(f"{self.name} company is not listed here")

    # Below are the methods2
    def greet(self):
        print(f"Welcome to {self.company} and your email_id is {self.email.lower()}")

# Below are the objects
Jeevan = Human("Jeevan",28,'KPIT')
Abhi = Human("Abhishek",30,"SoftClouds")

# Below are the accessing of class methods
# Jeevan.details_info()
# Abhi.greet()
# Jeevan.greet()
# Abhi.details_info()

# Accessing class attribute which are declared outside the objects/methods
print(Jeevan.__class__.place)


"""

"""
# Inheritance:
1.Inheritance allows us to define a class that inherits all the methods & Properties from another class
2. Parents Class is inherited from child class(base class)
3. Another words to say is --> Used for inherits all the methods and properties of another class


class Vehicle:

    def general_usage(self):
        print("general usage: Transportation")

class Car(Vehicle):

    def __init__(self):
        print("I am Car ")
        self.general_usage()
        self.wheel = 4
        self.has_roof = True

    def Special_usage(self):
        print("special usage: Commute to work: vacation with Family")

class MotorCycle(Vehicle):

    def __init__(self):
        print("I am Motor Cycle")
        self.general_usage()
        self.wheel = 2
        self.has_roof = False

    def Special_usage(self):
        print("special usage: Road trip, racing")

Car = Car()
Car.Special_usage()

Bike = MotorCycle()
Bike.Special_usage()

"""

# Multiple inheritance


"""
class Father:
    def father(self):
        print("My father name is Giriraj B S")
class Mother:
    def mother(self):
        print("My mother name is BABY")

class child(Father,Mother):  #Ftaher Mother is the base class
    def __init__(self,name):
        self.name = name
        print(f"my name is {self.name}")
        self.father()
        self.mother()
        Father.father(self)
        Mother.mother(self)

Jeevan = child("Jeevan")

"""

#Polymorphism

# Can be defined as a condition that occurs in many form
# 1. Operator level polyMorphism
# 2. Function level polyMorphism

# 1. Operator level polymorphism
# print(2+3)
# print('2'+'3')
# print('jeevan '*3)
# print('jeevan'* '3')

# 2. Function level Polymorphism
# len is an inbuilt function
# print(len("Program"))
# print(len(["python","Java","C"]))
# print(len({"name":"Jeevan","age":26}))


"""
# User defined exception using class

class accident(Exception):
    def __init__(self,msg):
        self.msg = msg

    def print_exception(self):
        print(f"User defined Exception: {self.msg} ")

try:
    raise accident("Crash between two vehicle")

except accident as e:
    e.print_exception()

finally:
    print("Please Don't Drink and Drive")
    
"""


