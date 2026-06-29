# object oriented programming languages

# class - blueprint of creating object 

# object- An object is an instance of a class

    
# Constructor -- __self__ Used to initialize object attributes.

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


# method -Functions defined inside a class.

#example    
'''
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

student1 = Student("Alice")
student1.greet()  

'''

#  4 pillers of object oriented programming languages [oops]

#  1 Inheritance- one class inherits another class

'''

Types of Inheritance 

*single - one child class  inherits one parent class

*multiple-  two or more parents class inhetrs one child class

*multilevel- A class inherts from the another inherited class 

*hierarical -multiple child class inherits from one child class 

*hybrid- comination of two orr more types of inheritance

'''

# 2  Polymorphism 

''' 
    compile time polymorphism -  method overloading  python does not support 
    runtime polymorphism - method overriding 
'''

# 3 Abstraction- Hiding implementation details and showing only essential features.

'''
  setter and getter methods 

  getter -read the Data
  setter -write the data

  setter--  A setter is a method used to change or update the value
  of a private (hidden) variable from outside the class.

  getter--  A getter is a method used to look at or read the value of 
  a private(hidden) variable from outside the class.

'''

#  4 Encapsulation
'''
  Two main pillers in encapsulation 

  data hiding
    the variables of a class are hidden from other classes..


  public access points
    the variables are hidden ,external code cannot chjange or read them directly 
    insteed we provide public methods llike setter  keys and getter keys .

     Encapsulation means wrapping your data and code together into a single package, like a capsule, 
     and hiding the inner workings from the outside world.
    ''' 
# Task 1

'''
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print(self.name,"say woof") 

dog1=Dog("puppy","golden retriver")
dog2=Dog("max","german shepherd")

print(dog1.name,"is a",dog1.breed)
print(dog2.name,"is a",dog2.breed)

dog1.bark()
dog2.bark()
'''
# task 2
'''
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        self.speed=0

    def accelerate(self,amount):
        self.speed+=amount
        print(self.color,self.brand,"accelerated to",self.speed,"km/h")

car1=Car("thar","black")
car2=Car("scoripo","white")

car1.accelerate(40)
car2.accelerate(50)
'''
'''
# task 3                 
class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.mark=0

    def add_mark(self,amount):
        self.mark+=amount
        print(self.name,"with roll no ",self.roll_no,"scored ",self.mark,"mark")

student1=student("snegan",79) 
student2=student("snt",31)

student1.add_mark(79)
student2.add_mark(99)
'''

