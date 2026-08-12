#List - otrder ,changable ,allow duplicates 
'''
a=["snt","sst",]
print(a)

#append 

a.append("extra")
print(a)
 
print(a[0])
print(a[2])
print(a[1])

#slicing

fruits=["apple","mango","orrange"]
print(fruits[1:3])
print(fruits[1:2])

numbers = [1,2,3,4,5,6,7,8]

#print(numbers[::2])
print(numbers[::3])
'''
#reverse the list
'''
numbers = [1,2,3,4,5]
# print(numbers[::-1])
del numbers[2]
print(numbers)

fruits=["apple","orange","mango"]
fruits.remove("apple")

fruits=["apple","orange","mango"]
fruits.pop(1)
print(fruits)

# delete the multiple values
numbers = [10,20,30,40,50]

del numbers[1:4]

print(numbers)

#Tuple  - order ,not chanageble, allows duplicates 

color=("orange","black","green")
print(color[-2])

#set -- unorder,changable ,no duplicate

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  

# add the element

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

'''
# Function 
'''def python():
    print("snt") 
def python():
    print("snt")
python()     

# parameter to allow data to passed into  the function
 
def python(name):
    print("hello",name)
python("snegan")    
'''
'''
def  python(a,b):
    print(a+b)    
python(10,20)    

'''
#Return Value   -  return sends a result back from a function
'''
def python(a,b):
    return a+b
result =python(10,20)
print(result) 
'''  
'''
#print function 
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)

# return function

def add(a, b):
    return a+b

result = add(10, 20)

print(result)

'''
'''
# scope  --- where  the variable can be use
# Local variable 
def show():
    x = 10
    print(x)

show()
# global scope 

x = 100

def show():
    print(x)

show()
'''
# sum of the list element  using loops

def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
data = [10, 20, 30, 40]
print(sum(data))

