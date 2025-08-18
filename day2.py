name=input("enter your name")
age=int(input("enter your age"))
print("hello:",name)
print("your age is:",age)
out put:
enter your namevyshu
enter your age18
hello: vyshu
your age is: 18

If/Else (Decision Making)
n=int(input("enter a number"))
if n%2==0:
    print("even number")
else:
    print("odd number")
out put:
enter a number 5
odd number

#Find maximum of two numbers
a=int(input("enter a first number"))
b=int(input("enter a second number "))
if a>b :
    print("maximum is :",a)
else:
    print("maximum is :",b)
output:
enter a first number13
enter a second number 23
maximum is : 23

#Check positive, negative, or zero
n=int(input("enter a number"))
if n>0:
    print("positive number")
elif n<0:
    print("negitive number")
else:
    print("zero")
  output:
enter a number 5
positive number
#Grade calculator
marks=int(input("enter your mark (0-100)"))
if marks >=90:
    print("grade a ")
elif marks >=75:
    print("grade b")
elif marks >=40:
    print("grade c")
else:
    print("fail")
output:
enter your mark (0-100) 30
fail

#Check Leap Year
n=int(input("enter a number"))
if n%4==0 and n%100==0 or  n%4==0:
    print("leap year")
else:
    print("not leap year")


Take two numbers and an operator (+, -, *, /) as input → perform the operation.
(Hint: use if conditions to check operator)
# Simple Calculator using if conditions
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero not allowed!")
else:
    print("Invalid operator! Please use +, -, * or /.")
OUT PUT:
enter a  first number45
enter a second number45
enter a operator(+, -, /,*):+
addition 90

#Code: Restaurant Bill with Discount



