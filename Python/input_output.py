#INPUT() STATEMENTS (EXAMPLE - 1)

# name = input("my name is:" )
# my_age = input("my age is:" ) 

# #converting (my_age) str to integer
# age = int(my_age)

#adding 1 to integer next_year_age to get next year age value

# next_year_age  = age + 1

# #printing customer output values

# print("Hello,", name + "!") # here + (concatenation)will use to join two string (str +str) values
# print("You are", age, "years old.")
# print("Next year your age will be", next_year_age, "years old." )


#INPUT() STATEMENTS (EXAMPLE - 2)

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# int_num1 = int(num1)
# int_num2 = int(num2)
# adding_numbers = int_num1 + int_num2

# print("Adding value is:" , adding_numbers)

#INPUT() STATEMENTS (EXAMPLE - 3)


# first_name = input("Enter your first name: ")
# second_name = input("Enter your second name: ")

# print("Welcome", first_name, second_name + "!")


# #INPUT() STATEMENTS (EXAMPLE - 4)

# age = input("Enter your age in years: ")
# int_age = int(age)

# # multiply the whole age with 12

# age_in_months = int_age * 12

# print("My age in months:", age_in_months)

# #INPUT() STATEMENTS CONVERTING INTO INT (EXAMPLE with int - 5)

# length = input("Enter the length of the rectangle: ")
# width = input("Enter the width of the rectangle: ")

# int_length = int(length)
# int_width = int(width)
# # Convert to float or int
# finding_are_of_rectangle = int_length * int_width
# print("Area of rectangle: ", finding_are_of_rectangle)

'''
'''#INPUT() STATEMENTS CONVERTING INTO FLOAT (EXAMPLE with float- 6)

# length = input("Enter the length of the rectangle: ")
# width = input("Enter the width of the rectangle: ")

# #input means str so we should convert float int

# new_length = float(length)
# new_width = float(width)
# total_area = new_length * new_width

# print("Area of the rectangle: ", total_area)
# '''

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#OUTPUT [ print() ] STATEMENTS
# t = (1,2,3,4,5)
# print(t)

#OUTPUT [ print() ] STATEMENTS -EXAMPLE 2
# name = input("your name: ")
# print("Hello",name,sep=", ",end="!")


#INTEGER OUTPUT [ print() ] STATEMENTS -EXAMPLE 1
# age = input("what's your age: ")
# #converting string into int
# age_int = int(age)
# print("Currently Iam", age_int, "years old",end= "...")


#INTEGER OUTPUT [ print() ] STATEMENTS -EXAMPLE-2
# num = input("Enter any number: ")
# #converting string into 
# num_int = int(num)
# print("You entered:",num_int,sep="")

#FLOAT OUTPUT STATEMENTS -EXAMPLE-3
# weight = input("Enter your weight: ")
# con_weight = float(weight)
# print("Currently my weight is:", con_weight, sep="")

#SUM OF MULTIPLE INPUTS # split(" ") # IN A SINGLE LINE -EXAMPLE-4
# a = input("enter the values: ")
# x,y,z = a.split(",") 
# #we should maintain this split value while writing the output("," "")
# sum = int(x) + int(y) + int(z)
# print("Sum of inputs:",sum, sep = "")

'''
#SPECIFYING SEPARATOR IN OUTPUT# split(" ") # -EXAMPLE-5
# inp = input()

# print("Name:",name,",Age:",age,sep = "")'''

#split() WORKS ON ONLY STRING VALUES NOT ON INTEGERS

# #END PARAMETER IN OUTPUT -EXAMPLE-6
# n = input("Enter 5 numbers separated by commas: ")  # Keep it as string
# a, b, c, d, e = n.split(",")  # Now split works
# print("countdown: ",a,b,c,d,e,sep=",")

# OR WE CAN WRITE IN DIRECT PRINT() STATEMENTS 

# n = int(input("enter n:"))
# print("Countdown: 5 4 3 2 1",end = " Blast off!")


#ARITHMETIC OPERATORS WITH input()
#input values: 10,5
# x,y = input("Enter a,b values: ").split(",")
# a = int(x)
# b = int(y)
# #In split "," is using to divide the input values
# print("Addition:",a+b,"Subtraction:",a-b,"Multiplication:",a*b,"Division:",a/b)

#input values: 20,5
# a,b = input("Enter your digits: ").split(",")
# x = int(a)
# y = int(b)
# #In split "," is using to divide the input values
# print("Addition:",x+y,",Subtraction:",x-y,",Multiplication:",x*y,",Division:",x/y,sep = "")

#COMPARISON OPERATORS WITH input()
# x,y = input("Enter your numbers: ").split(",")
# a = int(x)
# b = int(y)
# #Now we are printing comparison operators
# print("Greater than:",x>y,",Less than:",x<y,",Equal to:",x==y,",Not equal to:",x!=y,sep = "")

#FORMATTING OUTPUT USING f-strings
#expected output: Alice,25
# x,y = input("Enter your name and age:").split(",")
# #WE ARE USING f-string format in print() for output
# print(f"Name:{x},Age{y}")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

