
# Boolean  
a = 10
b = 20

print(a < b)
print(a > b)

# operation 
 
x=15
print(x==15)
print(x!=15)
print(x>=15)
print(x<=15)

mark=40
if(mark>90):
    print("grade A")
elif(mark>80):
    print("grade B")
elif(mark>70):
    print("grade c")
else:
    print("fail")        


# logical operation  AND  BOTH THE CONDITION MUST BE TRUE

age =20
citizen=True
if(age>18 and citizen):
    print("Eligible")
else:
    print("Not Eligible")     

# OR   ATLEAST ONE MUST BE TRUE 

age=20
citizen=True
if(age>21  or citizen):
    print("eligible")
else:
    print("not eligible")

# NOT   REVERSE THE RESULT


logged_in = True

if not logged_in:
    print("Please Login")
else:
    print("Welcome User")


#  Nested Conditions

age=30
license=True
if age>18 :
    if license:
        print("can drive")
    else:
        print("not drive")          
    print(" eligible")
else:
    print("not eligible") 

#  Number classifer

a=int(input("enter the number"))
if a>0:
    print("positive number")
elif a<0:
    print("negative number")   
else:
    print("0")
if a%2==0:
    print("even")
else:
    print("odd")    

# score

score=int(input("enter the number"))
if score>=90:
   print("a")
elif score>=80:
   print("b")     
elif score>=70:
   print("c")  
else:
   print("d")

# Login check

password = "snegan"
a = input("enter the value: ")
if a == password:
    print("Login")  
else:
    print("invalid password")   

# largest of three number

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)



    

