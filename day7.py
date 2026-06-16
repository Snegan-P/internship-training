
#Inheritance 
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
# single inheritance 
'''
class animal:
    def sound(self):
        print("animal make sound")
class dog(animal):
    def  bark(self):
        print("bark") 
d=dog()
d.sound()
d.bark()               
'''
# multiple inheritance
'''
class grandfather:
    def land(self):
        print("grand father buy a land" )
class father:
    def house(self):
        print("father buy a house")
class mother:
    def jewls(self):
        print("mother buy a jewls") 

class child(grandfather,father,mother):
    def bike(self):
        print("buy a bike")
c=child()

c.land()
c.house()
c.jewls()
c.bike()
'''
# Hierarchical inhetritance 
'''
class parents:
    def property(self):
        print("more")

class child1(parents):
    def child1(self):
        print("child")

class child2(parents):
    def child2(self):
        print("audlt")           
c=child1()
C=child2()
c.property
c.child1
C.child2
'''
'''
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Driving Car")


class Bike(Vehicle):

    def ride(self):
        print("Riding Bike")


c = Car()
c.start()
c.drive()

b = Bike()
b.start()
b.ride()     
'''
# hybrid 

'''
class Grandfather:
    def land(self):
        print("land")

class Father(Grandfather):
    def house(self):
        print("house")

class Mother:
    def jewels(self):
        print("jewels")

class Child(Father, Mother):
    def bike(self):
        print("bike")

c = Child()

c.land()
c.house()
c.jewels()
c.bike()
'''
# Multilevel
'''
class Grandfather:
    def land(self):
        return "land"

class Father(Grandfather):
    def house(self):
        return "house"

class Son(Father):
    def car(self):
        return "car"

s = Son()

print(s.land())
print(s.house())
print(s.car())
'''
# polymorphism

# method overriding-run time polymorphism

'''
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

# Abstraction 

# getter method 
'''
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

'''

# getter method

'''

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
    def __init__(self,brand)        

'''
# Encapsulation 
class Bankaccount:
    def __init__(self):
        self.__balance=0.0

    def deposit(self,amount):
        if amount>0:
            self.__balance +=amount
        else:
            print("invalid")

    def get_balance(self):
        return self.__balance

account=Bankaccount()
account.deposit(500)
print("current balance:",account.get_balance())                    




