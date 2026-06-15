# object oriented programming languages

# class - blueprint of creating object 

# object- An object is an instance of a class
    
# constructor -- __self__ Used to initialize object attributes.
#example    
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)

print(student1.name)  
print(student1.age)   
'''
'''
# method -Functions defined inside a class.
#example    
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

student1 = Student("Alice")
student1.greet()  

'''
# Inheritance- one class inherits another class

'''
Types of Inheritance 

*single - one child class  inherits one parent class

*multiple-  two or more parents class inhetrs one child class

*multilevel- A class inherts from the another inherited class 

*hierarical -multiple child class inherits from one child class 

*hybrid- comination of two orr more types of inheritance
'''
'''

class Bank:
    def deposit(self):
        print("Deposited")

class SavingsAccount(Bank):
    def interest(self):
        print("Intrested Added")

s = SavingsAccount()

s.deposit()
s.interest()

'''
# Polymorphism - method overloading - compile time polymorphism - python does not support method overloading 

'''
# method overriding-run time polymorphism
class Animal:
    def sound(self):
        return "Animal Sound"

class dog(Animal):
    def sound(self):
        return "Bow Bow"

class cat(Animal):
    def sound(self):
        return "Meow Meow"

d = dog()
c = cat()

print(d.sound())
print(c.sound())
'''
# Abstraction- Hiding implementation details and showing only essential features.
# getter method 
class vechile:
    def __init__(self,brand):
        self.__brand=brand

    def get_brand(self):    
        return self.__brand
    
    def start(self):
        pass

class Car(vechile):
    def start(self):
        print("car is start") 

class Bike(vechile):
    def start(Self):
        print("bike is start") 

c=Car("thar")
b=Bike("enfiled")

c.start()
b.start()

# getter method

class vechile:
    def __init__(self,brand):
        self.__brand=brand
        self.__speed=0

    def get_brand(self):
        return self.__brand
    
    def get_speed(self):
        return self.__speed     
    
    def set_speed(self,speed):
        if speed>=0:
            self,__speed=speed
        else:
            print("error")
class bike(vechile):
    def __init__(self,brand,)            



# Encapsulation-  Bundling data and methods together and controlling access.
