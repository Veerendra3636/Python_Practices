
#if-elif-else statement : Example-1
# Check if weather and time_of_day 
'''weather = input()
time_of_day = input()

if weather == "sunny":
    print("you can play with your toy")

elif weather == "rainy":
    print("you can play with you boat toy")

elif weather == "snowy" and time_of_day == "night":
    print("You can play with your teddy bear toy")

else:
    print("you can play with your robot toy")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-2
#   Check if a number is positive, negative, or zero

'''num = int(input("enter number: "))
if num>0:
    print("positive number")

elif num<0:
    print("Negative Number")

else:
    print("Zero")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-3
#Check grade based on marks

'''marks = int(input("Enter your marks: "))
if marks>90:
    print("Grade A")

elif marks>75:
    print("Grade B")

elif marks>60:
    print("Grade C")

else:
    print("your are failed in this exam")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-4
#Check if age fits into child, teen, or adult

'''age = float(input("enter your age: "))

if age<= 12:
    print("Child")

elif age<= 19:
    print("Teenage")

else:
    print("Adult")'''


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-5
#Temperature check: cold, normal, or hot

'''temperature = int(input("Enter the temperature: "))

if temperature <=20:
    print("COLD")

elif temperature <= 35:
    print("NORMAL")

else:
    print("HOT")'''


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-6 
#Check if a number is divisible by 3, 5, or 

'''
num = int(input("Enter the number: "))

if num % 3 == 0:
    print("divisible by 3")

elif num % 5 == 0:
    print("Number divisible by 5")

else:
    print("number can not divisible by 3 or 5")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-7 
#Simple calculator (add, subtract, multiply)

'''op = input("choose operation (+, -, *): ")
a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))

if op == "+":
    print("result of:", a+b)

elif op == "-":
    print("result of:", a-b)

elif op == "*":
     print("result of:", a*b)

else:
    print("Invalid operation")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-8 
#Traffic light system

'''color = input("Enter the color: ")

if color == "red":
    print("STOP")

elif color == "yellow":
    print("ready to go")

elif color == "green":
    print("GO")

else:
    print("Invalid color")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if-elif-else statement : Example-9 
#Login system with different users

user = input("enter user name: ")

if user == "admin":
    print("Hello, Welcome Admin!")

elif user == "guest":
    print("Hello, Welcome Guest!")

else:
    print("Invalid User")