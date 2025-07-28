#SIMPLE CALCULATOR PROGRAM
operator = input("select any operator(+, -, /, *): ")
num1 = int(input("Enter your num1: ")) 
num2 = int(input("Enter your num2: ")) 
#now we will write the conditions

if operator == "+":
    print(f"Adding of num1 and num2:{num1+num2}")
    
elif operator == "-":
    print(f"Subtraction of num1 and num2: {num1-num2}")

elif operator == "*":
    print(f"Multiplication of num1 and num2: {num1*num2}")

elif operator == "/":
    print(f"Division of num1 and num2: {num1/num2}" )

else:
    print("You selected a wrong operator")