#NESTED IF STATEMENTS
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#NESTED IF - EXAMPLE:1

'''weather = input("how is weather: ")
time_of_day = input("which time: ")

if weather == "normal":
    
    if time_of_day == "morning":
        print("You can play cricket")

    else:
        print("you can not play cricket")


elif weather == "rainy":
    print("you can play with your boat toy")


elif weather == "snowy":
    if time_of_day == "afternoon":
        print("you can play with your snowman toy")


    else:
        print("you can not play with your snow toy")


else:
    print("weather is not good, you can not play now")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#NESTED IF - EXAMPLE:2
# Check if number is positive and even

'''num = int(input("enter the number: "))
if num>0:
    if num % 2 == 0:
        print("Number divisible by 2")

    else:
        print("Number can not divisible by 2")
        
else:
    print("this not a Higher value")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#NESTED IF - EXAMPLE:3
# Check eligibility to vote and age group
'''
age = int(input("age: "))

if age>= 18:
    
    if age>= 60:
        print("you are senior citizen, you can vote")

    else:
        print("as you are an adult, you can also vote")

else:
    print("as you are minor, you can not vote right now")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#NESTED IF - EXAMPLE:4
# Password and OTP check

'''password = input("enter your password: ")

if password == "admin":

    otp = int(input("Enter OTP: "))

    if otp == 1234:
        print("your verified customer")

    else:
        print("your are entered wrong OTP")

else:
    print("You entered wrong password")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#NESTED IF - EXAMPLE:5
# Check marks and grade
'''
marks = int(input("Enter your marks: "))

if marks>=35 and marks<=100: #HERE WE USED "and"(Logical operator)
    
    if marks >= 90:
        print("GRADE A")

    elif marks >=75:
        print("GRADE B")

    elif marks >= 35:
        print("GRADE C")

else:
    print("your failed in exams")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#NESTED IF - EXAMPLE:6
# ATM pin and balance check

'''pin = int(input("Enter your pin: "))

if pin == 4444:
    print("you entered correct pin.")

    balance = int(input("Enter amount: "))
    
    if balance ==1500:
        print("Transaction approved.")

    else:
        print("you dont enough money in your a/c")

else:
    print("Invalid Pin")'''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#NESTED IF - EXAMPLE:7
# Check exam result: pass/fail + distinction

'''marks = int(input("Enter your marks: "))

if marks >=35:
    print("you are pass")

    if marks >= 85:
        print("Distinction")

else:
    print("you are failed")'''


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#NESTED IF - EXAMPLE:8
#Check admission eligibility (age + marks)

age = int(input("Enter your age: ")) 
if age >= 18:
    marks = int(input("Enter your marks: "))
    
    if marks>=60:
        print("you are eligible another sem")

    else:
        print("marks not enough")

else:
    print("you are not eligible")