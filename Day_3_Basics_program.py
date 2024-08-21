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

# Inheritance

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