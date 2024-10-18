
int(123.987)
print(int('10'))
#print(int('10.5))
#print((10+5j))
#print(("ten"))
#print(int("0B1111"))
print(int(True))
print(int(False))
print(int('0B1010',2))
print(int('0O12',8))
print(int('0XA',16))


print("                                         ")
print("-----------------------------------------")
print("                                         ")


print(bool(0))
print(bool(1))
print(bool(20))
print(bool(13.5))

s="You're\n mine"
print(s)

str1 = "HelloWorld"
print(str1[1:8:2])

print("Hello" + "World")
print("Hello\n" * 3)

s= "Hello"
print(s[0])
print(s[1])
print(s[-1])
#print(s[10])
print(s[1:40])
print(s[1:])
print(s[:4])
print(s[:])
print(s*3)
print(len(s))

print(s.title())
print(s.upper())
print(s.lower())

lang=' Python '
print(lang.rstrip())
print(lang.lstrip())
print(lang.strip())

print(str(10))
print(str(10.5))
print(str(10+5j))
print(str(True))
print(str(False))


print("                            ")
print("-----------------------------------------")
print("                            ")


list1 = [10,20,30,40,50]
list1[0] = 100
print(list1)

list2 = [10,20,30,40,50]
list2[1:4] = [100,200,300]
print(list2)

list3 = [10,20,30,40,50]
list3[1:4] = [100,200,300,400,500,600]
print(list3)

ls=[20,5.5,'abc',True,20]
print(ls)

list4 = [10,20,30,40,50]
print(list4[1])
print(list4[-1])
print(list4[1:3])
list4[0]=100
print(list4)
print(type(list4))

t1 = (10,20,30,40,50)
print(t1)
print(type(t1))
print(t1[1])
print(t1[-1])
#t1[0]=100
print(t1)

print("                Sets               ")
print("-----------------------------------------")
print("                            ")

s1 = {10,20,30}
print(s1)

s2 = {10,20,30,'abc'}
print(s2)

print("           Dictionary               ")
print("-----------------------------------------")
print("                            ")

d1 = {'Saurabh':1,'Alexa':2,'Hitarth':3}
print(d1)
print(type(d1))
print(d1['Saurabh'])

print(type(None))
var1 = None
print(var1)
 
print("CONSTANT")
print("-----------------------------------------")
print("                            ")


MAX = 10
print(MAX)




print("Escape Characters")
print("-----------------------------------------")
print("                            ")

#/n New Line
print("Hello\nWorld")

# /t Horizontal Tab
print("Hello\tWorld")

# /b Backspace
print("Hello\bWorld")

# /r Carriage Return
print("Hello\rWorld")

# /f Form Feed
print("Hello\fWorld")

# /v Vertical Tab
print("Hello\vWorld")

# /a Alert
print("Hello\aWorld")

  




print("Operators")
print("-----------------------------------------")
print("                            ")

#Arithmetic Operators
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#Unary Operators
a=10
print(a)
print(+a)
print(-a)

#Relational Operators
a=10
b=20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


#Logical Operators
a=10
b=20
print(a and b)
print(a or b)
print(not a)
print(not b)

print(" ")
print("-----------------------------------------")
print(" ")

#Bitwise Operators
a=10
b=20
print(a&b)
print(a|b)
print(a^b)

print(" ")
print("-----------------------------------------")
print(" ")

#Assignment Operators
a=10
b=20
a+=b
print(a)

print(" ")
print("-----------------------------------------")
print(" ")

#Special Operators
a=10
b=20
print(a is b)
print(a is not b)

print(" Precedence of Operators ")
print("-----------------------------------------")
print(" ")

x = 1+2**3/4*5
print(2*'Yes'+3*'!')
print(type(1+5))
print(type(1+5.0))
#print(type(1+'5'))
print(type('1'+'5'))
print(2+3*5/5)
print(3+2**2**3)

print('  Repetition of Operator  ')
print('-----------------------------------------')
print('')

print(2*'Hello')
print(3*'!')


print('Relational Operators')
print('-----------------------------------------')
print('')

a="Hello"
b="Hello"
print("a>b is ",a>b)
print("a<b is ",a>=b)
print("a<b is ",a<=b)
print("a==b is ",a==b)
print("a!=b is ",a!=b)


print(" Logical Operators ")
print("-----------------------------------------")
print("")


print(10 and 20)
print(10 or 20)
print(not 10)
print(not "Hello")
print(not 0)
print(not "")


print(" Assignment Operators ")
print("-----------------------------------------")
print("")


a=10
b=20

a += b
print(a)

a -= b
print(b)



print(" Multiple Assignment ")
print("-----------------------------------------")
print("  ")

a,b,c=1,2,3
a,b,c=10,20,30


#WAP to caluclate area and perimeter of a rectangle 

pi = 3.141
r = 45
area = pi*r*r
perimeter = 2*pi*r
print("Area of the circle is", area)
print("Perimeter of the circle is", perimeter)


#WAP to computer simple interest

p = 1000
r = 10
t = 20
si = (p*r*t)/100
print("Simple Interest is", si)

#WAP to find average of three numbers
a = 10
b = 20
c = 30
avg = (a+b+c)/3
print("Average of the three numbers is", avg)

#WAP to find area of cuboid

l = 10
b = 20
h = 30
area = 2*(l*b + b*h + h*l)
print("Area of the cuboid is", area)

#WAP to find area of a circle

r = 45
area = pi*r*r
print("Area of the circle is", area)

#WAP to find volume of a sphere

r = 45
volume = (4/3)*pi*r*r*r
print("Volume of the sphere is", volume)



print("              Input and Output                     ")
print("----------------------------------")
print(" ")




print()
print("Hello")
print("Hello \n World")
print("Hello" + "World")
print("Hello", "World")


name = "Alice"
age = 30
print("Name", name, "Age", age)


a,b = 2,4
print(a,b)
print(a,b,sep=',')
print(a,b,sep=':')
print(a,b,sep='- - -')



print("Conversion types")


#d% - integer
#i% - integer
#f% - float
#s% - string
#%x - hexadecimal
#%o - octal

 
x = 10 
print("value of %i" %(x))


x,y = 10,20
print("value of %i y=%d" %(x,y))


name = "ABC"
print("Hi %s" %(name))
print("Hi (%20s)" %(name))
print("Hi %20s" %(name))
print("Hi (%-20s)" %(name))

print("Hi %c, %c" %(name[0], name[1]))
print("Hi %s " %(name[0:2]))


print("Input")
print("----------------------------------")
print(" ")

num = 123.4567898
print("value is %f" %(num))
print("value is %e" %(num))
print("value is %g" %(num))
print("value is %0.2f" %(num))
print("value is %0.5f" %(num))


print("%o" %(16))
print("%x" %(16))


n1,n2,n3 = 10,20,30
print("num1={0}, num2={1}, num3={2}".format(n1,n2,n3))


print("num1={2}, num2={1}, num3={0}".format(n1,n2,n3))


print("num1={one}, num2={zero}, num3={two}".format(zero=n1,one=n2,two=n3))


print("num1={2}, num2={0}, num3={1}".format(n1,n2,n3))


print("")
print("----------------------------------")
print("")


print("Sam has {0} red balls, {1} yellow balls".format(12,31))
print("Sam has {1:d} red balls, {0:d} yellow balls".format(12,31))
print("We are the {} who say {}!".format("knights","ni"))
print("The story of {0}, {1}, and {other}".format("Bill","Manfred",other="Georg"))

print("")
print("----------------------------------")
print("F String")

name="Abc"
print(f"Hello {name}")

balance=1550.34342
print(f"My name is {name} and my balance is {balance:.2f}")


print("")
print("----------------------------------")
print("Inputs")

#str = input("Enter an int number")
#print(str)
#print(type(str))

#num1=int(str)
#print(num1)
#print(type(num1))


#a,b=input("Enter two values").split()
#print("First value is",a)
#print("Second value is",b)
#print("Values are",a,b)


#a,b,c=map(int,input("Enter three values").split())
#print(a,b,c)


#WAP to accept two numbers and find thier sum and product

#a,b=map(int,input("Enter two values").split())
#print("Sum is",a+b)
#print("Product is",a*b)


#WAP to accept length and breadth of a rectangle and calculate the area and perimeter

#l,b=map(int,input("Enter length and breadth of a rectangle").split())
#print("Area is",l*b)
#print("Perimeter is",2*(l+b))


#WAP to compute simple interest

#p,r,t=map(int,input("Enter principal, rate and time").split())
#si=(p*r*t)/100
#print("Simple Interest is",si)



#WAP to find average of three numbers

#a,b,c=map(int,input("Enter three numbers").split())
#avg=(a+b+c)/3
#print("Average is",avg)



#WAP to find average of three numbers

#a,b,c=map(int,input("Enter three numbers").split())
#avg=(a+b+c)/3
#print("Average is",avg)



#WAP to find area of a cuboid

#l,b,h=map(int,input("Enter length, breadth and height of a cuboid").split())
#area=2*(l*b+b*h+h*l)
#print("Area of the cuboid is",area)



#WAP to find area of a circle

#r=int(input("Enter radius of a circle"))
#area=pi*r*r
#print("Area of the circle is",area)



print("")
print("----------------------------------")
print("CONDITIONAL STATEMENTS")


#a=10
#b=20
#if a>b:
    #print("a is greater than b")
#else:
#    print("b is greater than a")


# Example of if statement
#ch1= input("Enter single character")
#if ch1>='0' and ch1<='9':
#    print("you entered a digit")



# TASK

## Q1.


# Example of if-else

# n1,n2=map(int, input("Enter two intergers").split())

#if(n1%n2==0):
#    print(f"{n1} is divisible by {n2}")
#else:
#    print(f"{n1} is not divisible by {n2}")
    
#output integers are 12, 5 
# 12 is not divisible by 5


## Q2.


 # Example of If-elif-else
#amt=int(input("Enter sale amount"))

#if amt>30000:
    #discount=amt*0.20
#elif amt>=20000:
    #discount=amt*0.15
#elif amt>=10000:
    #discount=amt*0.10
#else:
    #discount=amt*0.5
    
#print(f"You have received discount of Rs {discount}")
#output id amt = 30000
#You have received discount of Rs 6000


## Q3.


#Example of nested if
#x,y,z=map(int, input("Enter three integers ").split())
#min=mid=max=None

#if x<y and x<z:
    #if y<z:
        #min,mid,max=x,y,z
#    else:
        #min,mid,max=x,z,y
#elif y<x and y<z:
    #if x<z:
#        min,mid,max=y,x,z
#    else:
#        min,mid,max=y,z,x
#else:
    #if x<y:
#        min,mid,max=z,x,y
#    else:
#        min,mid,max=z,y,x
        
#print(f"Number in ascending order {min}, {mid} , {max})")
#output when x=20,y=30,z=40
# Numbers  in ascending order 20,30,40


# Problem Solving

## WAP( Write a program ):-

## To print “i have a brought _ _ in Rs _”

### format


#print("i have brought {} {} in Rs{}".format("6","mangoes ", "220.50"))
#output
# i have brought 6 mangoes  in Rs220.50


### Modulo


#num=6
#fr="mangoes"
#cost=220.50

#print("i have brought %i %s in Rs %i" %(num,fr,cost))
#output
# i have brought 6 mangoes in Rs 220


### F-string/F-function


#num=6
#fr="mangoes"
#cost=220.50

#print(f"I have brought {num} {fr} in Rs {cost}")
#output
# I have brought 6 mangoes in Rs 220.5


print("")
print("----------------------------------")
print("")


a,b=10,20
print("both a and b are equal"if a==b else "a is greater than b" if a>b else "b is greater than a")

if a==b:
    print("a and b are equal")
elif a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


print("")
print("----------------------------------")
print("     Match Case     ")


# num = int(input("Enter a number"))
#  match num:
#    case 1:
#        print("One")
#    case 2:
#        print("Two")
#    case 3:
#        print("Three")
#   case _:
#        print("Number not between 1 and 3")


# ch2= input("enter a character")
# match ch2:
#    case 'a' | 'e'| 'i' | 'o' | 'u':
#        print(f"{ch2} is a vowel")
#    case _:
#        print(f"{ch2} is not a vowel")


# ch2= input("enter a character")
# if ch2== "a" or ch2=="e" or ch2=="i" or ch2=="o" or ch2=="u":
#        print(f"{ch2} is a vowel")
# else:
#       print(f"{ch2} is not a vowel")



# print("")
# print("----------------------------------")
# print("     Practice Problems     ")


# WAP to check whether a number is even or odd

# num=int(input("Enter a number"))
# if num%2==0:
#     print(f"{num} is even")
# else:
#    print(f"{num} is odd")


# WAP to check whether person is eligible for voting or not

#age=int(input("Enter your age"))
#if age>=18:
#    print("You are eligible for voting")
#else:
#    print("You are not eligible for voting")


# WAP to enter a number between 1 to 7 and print the name of the day

# num=int(input("Enter a number between 1 to 7"))
# if num==1:
#     print("Monday")
# elif num==2:
#     print("Tuesday")
# elif num==3:
#     print("Wednesday")
# elif num==4:
#     print("Thursday")
# elif num==5:
#     print("Friday")
# elif num==6:
#     print("Saturday")
# elif num==7:
#     print("Sunday")
# else:
#     print("Invalid input")


# WAP to check whether a year is a leap year or not. A year is a leap year if any of the following conditions are satisfied:
# 1. The year is divisible by 400
# 2. The year is divisible by 4 and not divisible by 100

# year=int(input("Enter a year"))
# if year%400==0:
#     print(f"{year} is a leap year")
# elif year%4==0 and year%100!=0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# WAP to calculate to take in the marks of 5 subjects, compute average display the grade as per following rules:
# 1. average>=90%: "A"
# 2. average>=80%: "B"
# 3. average>=70%: "C"
# 4. average>=60%: "D"

# english,maths,physics,marathi,chemistry=map(int,input("Enter marks of 5 subjects").split())
# avg=(english+maths+physics+marathi+chemistry)/5
# if avg>=90:
#     print("A")
# elif avg>=80:
#     print("B")
# elif avg>=70:
#     print("C")
# elif avg>=60:
#     print("D")
# else:
#     print("F")


# WAP to take a single digit number from keyboard and print it in word using if elif

#num=int(input("Enter a single digit number"))
# if num==0:
#     print("Zero")
# elif num==1:
#     print("One")
# elif num==2:
#     print("Two")
# elif num==3:
#     print("Three")
# elif num==4:
#     print("Four")
# elif num==5:
#     print("Five")
# elif num==6:
#     print("Six")
# elif num==7:
#     print("Seven")
# elif num==8:
#     print("Eight")
# elif num==9:
#     print("Nine")
# else:
#     print("Invalid input")


# WAP to take a single digit number from keyboard and print its value in english word using match case

# num=int(input("Enter a single digit number"))
# match num:
#     case 0:
#           print("Zero")
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case 5:
#         print("Five")
#     case 6:
#         print("Six")
#     case 7:
#         print("Seven")
#     case 8:
#         print("Eight")
#     case 9:
#         print("Nine")
#     case _:
#         print("Invalid input")



# print("")
# print("----------------------------------")
# print("     For Loop     ")    

# str="Hello world"
# for x in str:
#    print(x, end=' ')

# print("")
# print("----------------------------------")
# print("     Range Data Type     ")    

# r=range(10)
# for i in r: print(i, end=' ')


#WAP to find sum of first n numbers using for loop

# n=int(input("Enter a number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("Sum of first",n,"numbers is",sum)


#WAP to find multiplication of first n numbers using for loop

# n=int(input("Enter a number"))
# mul=1
# for i in range(1,n+1):
#     mul=mul*i
# print("Multiplication of first",n,"numbers is",mul)


#WAP to display numbers from 15 to 1 in descending order

# for i in range(15,0,-1):
#     print(i, end=' ')


#WAP to find factorial of a number using for loop

# n=int(input("Enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("Factorial of",n,"is",fact)


#WAP to display odd numbers between 10 to 30 using for loop

# for i in range(11,30,2):
#     print(i, end=' ')


#WAP to display sum of even numbers between 30 to 50

# sum= 0
# for i in range(30,51):
#     if i%2==0:
#         sum=sum+i
# print("Sum of even numbers between 30 to 50 is",sum)


# print("Odd numbers between 10 and 30:")
# for i in range(11, 31, 2):
#      print(i, end=' ')






# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#    print("%s %d" %(i, d[i]))


# print("\nSet Iteration")
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i, end=' ')



# WAP to sum numbers from 1 to 10


sum=0
i = 1
while i <= 10:
    sum += i
    i += 1
print("Sum of numbers from 1 to 10 is", sum)    



print("")
print("----------------------------------")
print("")


# WAP to find sum from n1 to n2
# n1=int(input("Enter n1"))
# n2=int(input("Enter n2"))
# sum=0
# i = n1
# while i <= n2:
#     sum += i
#     i += 1
# print("Sum of numbers from",n1,"to",n2,"is",sum)    


# count=0
# print('Enter correct username and password combo to continue')
# while count < 3:
#     name,pwd=input("Enter Name and password").split()
#     if name=="stud" and pwd=='pass':
#         print('Access granted')
#         break
#     else:
#         if count==2:
#             print('Sorry, Attempts completed')
#         else:
#             print('Access denied. Try again.')
#         count += 1


print("")
print("----------------------------------")
print(" Infinte Loop and Break ")

# from random import randint
# LOW,HIGH= 1, 10
#  secret_number = randint(LOW,HIGH)
#  clue = ""
# while True:
#     guess = input(f"Guess the number between {LOW} and {HIGH} {clue} ")
#     number = int(guess)
#     if number > secret_number:
#         clue = f"(Number is less than {number})"   
#     elif number < secret_number:
#         clue = f"(Number is less greater than {number})"
#     else:
#         break

# print(f"You guessed it! The secret number is {number}")


print("")
print("----------------------------------")
print(" Nested Loop ")


for i in range(4):
    for j in range(4):
        print(f"i={i}, j={j}")


for i in range(2):
    for j in range(4):
        print(f"i={i}, j={j}")


print("")
print("----------------------------------")
print(" #Pyramid star pattern ")


# rows = int(input("Enter number of rows: "))
#  for i in range(0, rows):
#    for j in range(rows - i - 1):
#        print(" ", end="")
#    for j in range(2 * i + 1):
#        print("*", end="")
#    print()


print("")
print("----------------------------------")
print(" Break statement ")


for x in range(10):
    if x > 5:
        break
    print(x, end=" ")


# Continue Statement

sum=0
for i in range(21):
    if i in range(5,15):
        continue
    sum += i
print(sum)


# Pass statement

# x = int(input("Enter a number: "))
# if x >= 0:
#     pass
# else:
#     print("The number is negative")


# for loop with else clause

for x in range(10):
    if(x>5):
        break
    print(x, end=" ")
else:
    print("Finally finished!")


# Examples of for loop with else clause

# ls=[10,20,30,40,50,60,70]
# search_ele=int(input("Enter a number"))
# for ele in ls:
#    if search_ele == ele:
#        print("Element found")
#        break
# else:
#    print("Element not found")

l1=list(range(0,10,2))
print(l1)
print(type(l1))


print(" ")
print("----------------------------------")
print(" ")


