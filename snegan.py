
#swap                          1
'''
a=10
b=20
a,b=b,a
print("a=",a)
print("b=",b)
'''
#smallest no                   2
'''
numbers=[1,2,3,4,5]
smallest=numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
print(smallest)    
'''

#count                         3

'''
num=1234
count=0
while num>0:
    count+=1
    num //=10
print(count) 

'''
#leap year                     4

'''
year=2004
if(year%4==0 and year%100!=0) or year%400==0:
    print("leap  year")
else:
    print("not leap year")    
'''

#check anagram                 5

'''
s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print("anagrams")
else:
    print("not anagrams")

'''

# sequence of number             6

'''
numbers = [1, 2, 3, 5]

n = 5

expected = n * (n + 1) // 2      
actual = sum(numbers)

print(expected - actual)

'''
#sequence of characters          7

'''   
text="snegan" 
char="n"
print(text.count(char))
 
 '''

# frahrenheit to celsuis           8

'''
celsuis=24
frahrenheit=celsuis*9/5+23
print(frahrenheit)
'''

#leep year                         9

'''
a=int(input("enter the year"))
if a % 4 == 0:
    print("leep year")
else:
    print("Not a Leap year")
'''
# balance                        10

'''
balance = 10000

amount = int(input("Enter Withdrawal Amount: "))

if amount <= balance:

    if amount % 100 == 0:
        print("Transaction Successful")
        balance = balance - amount
        print("Remaining Balance =", balance)

    else:
        print("Amount should be multiple of 100")

else:
    print("Insufficient Balance")
'''
#  elighible                      11

'''
age=int(input("enter the age"))
weight=int(input("enter the weight"))

if age>=18 and weight>=50:
    print("eligible to donate the blood")
else:
    print("not eligibe to donate the blood")
'''
# divisible                       12
'''
a=int(input("enter the number"))
if  a % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
'''

#divisible by 3 and 5               13

'''
a=int(input("enter the number"))
if a%5==0 and a%3==0:
    print("divisible")
else:
    print("not divisible")
'''
# absolute vlue                       14
'''
a=int(input("enter the number"))
if a < 0:
    a=-a
print("absoulute vale:",a)   
'''
# factorial                           15
'''
num = int(input("Enter Number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)
'''

#function                            16
'''
def add(a,b):
    result=a+b
    return result
obj=add(10,20)
print(obj)
'''
#local scope                        17
'''
def a():
    a=10
    print(a)
a()   
'''
#global scope                       18
'''
a=10
def show():
    print(a)
show()
print(a)
'''
# local and global scopr            19
'''
a = 10

def show():
    b = 10
    print("in")
    print(a)
    print(b)

show()

print("out")
print(a)

'''# List  
'''
student={
    "name":"snegan"
    "age":22
}
print(student)
'''

print("snt")
