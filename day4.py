<<<<<<< HEAD
print("snt")
=======
#for loops
#integer
'''
for i in range(1,11,2):
    print(i)
'''    
# multiple times 
'''
for i in range(3):
    print("Snegan")
'''    
#
'''
for i in range(1,10,2):
    print(i)
'''   
# patterns
'''
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()            
'''
# box pattern 
'''
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")  
    print()          
'''   
#  triangle pattern
'''
for i in range(5):
    for j in range(5):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()       
'''
# square pattern
'''
for i in range(5):
    for j in range(5):
        if j>=i:
            print("*",end=" ")
        else:
            print("*",end=" ")
    print()
'''
# traingle 
'''
for i in range(5):
    for j in range(5):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()     
'''
# inverted traingle  
'''
for i in range(5):
    for j in range(5):
        if j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()     
'''
#
'''
for i in range(5):
    for j in range(5):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()     
'''
# left traingle 
'''
for i in range(5):
    for j in range(5):
        if j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()     
'''
 # number traingle 
'''
for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
'''
'''
for i in range(5):
    for j in range(5-i):
        print(j+1, end=" ")
    print()    

'''
#while loop
'''
num =5
while(num>0):
    print("code")
    num-=1
'''
'''
list=[1,2,3,4,5]
while list:
    print("hi snt")
    list.pop()
'''   
 #print 10 no
''''
i = 1

while i <= 10:
    print(i)
    i += 1
'''
'''
i=10
while i>=1:
    print(i)
    i-=1
  '''
# multiplication table
'''
s=int(input("enter the number: "))
i=1
while i<=10:
    print(s,"x",i,"=",s*i)
    i +=1
'''
# Even numbers
'''
i=2
while i<=20:
    print(i)
    i+=2
 '''   
# odd numbers 
'''
i=1
while i<25:
    print(i)
    i+=2
'''
#factorial 
'''
num=int(input("enter the number"))
fact=1
i=1
while i<=num:
   fact*=i
   i+=1
print("factorial=",fact)  
'''  
#count digits
'''
num=int(input("enter number"))
count=0
while num>0:
    count+=1
    num//=10
print("Digits=",count)    
'''
#reverse the digits

''' 
num=int(input("enter the number: "))
reverse=0
while num > 0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print(reverse)   
'''
'''
password = "snt"
attempt = 1

while attempt <= 3:
    user = input("Enter password: ")

    if user == password:
        print("Login Success")
        break

    print("Wrong Password")
    attempt += 1

if attempt > 3:
    print("Account Blocked") 
'''    
#     FizzBuzz for 1-50 (Fizz/Buzz/FizzBuzz rules)
'''
for i in range (1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")  
    else:
        print(i)              
'''
# game 

target = 25

guess = int(input("Enter the number: "))

while guess != target:

    if guess < target:
        print("Too Low")

    else:
        print("Too High")

    guess = int(input("Try Again: "))

print("Correct Guess!")



>>>>>>> feature-login
