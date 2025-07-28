#if -else statement : Example-1
#Check if a person is adult (age ≥ 18)
'''age = int(input("Enter your age: "))
if age>= 18:
    print("you are eligible for this role")
    
else:
    print("you are not eligible for this role")
    '''
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-2
# Check if a number is positive or negative
'''
num = int(input("Enter the number: "))
if num<0:
    print("this is negative number")

else:
    print("you entered positive number")
'''
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-3
# Check if a number is even or odd

'''num = 7
if num%2 == 0:
    print("even")

else:
    print("odd")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-4
# Check if a person is adult or minor
'''age = int(input("Enter your age: "))
if age>=16:
    print("You are an Adult")

else:
    print("your are a minor")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-4
# Check if password is correct

'''
password = input("enter your password: ")

if password == "admin":
    print("your password is correct")

else:
    print("you entered incorrect password")
    '''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-5
# Check if a string is empty
'''text =  input("")
if text == "":
    print("this is empty string")

else:
    print("you entered some text")
'''
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-6
# Check if user entered a number greater than 100
'''
number = int(input("Enter the number: "))

if number>100:
    print("U entered above 100")

else:
    print("You entered below 100")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#if -else statement : Example-6
# Compare two numbers

'''num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number: "))

if num1>num2:
    print("num1 is greater than num2")

else:
    print("num1 is less than num2")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-7
# Check if temperature is cold or hot

'''weather = float(input("Enter temperature: "))
if weather<20:
    print("cold weather")

else:
    print("hot weather")
'''
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-7
# Check if a number is divisible by 3

'''number = int(input("enter the number: "))

if number % 3 == 0: 
# % modulo means reminder value so reminder is 0 than it can be divisible
    print("number divisible by 3")

else:
    print("Number can not divisible by 3")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#if -else statement : Example-8
# Check if a word is “python” (case-insensitive)

word = input("Enter the word: ")

if word == "python":
    print("Correct word!")

else:
    print("You entered wrong word")