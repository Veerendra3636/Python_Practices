#FINDING THE SUM OF TWO NUMBERS
#Sample input: num1 = 5, num2 = 10

'''WE CAN'T WRITE LIKE THIS BECAUSE, int() can't convert a list
— it can only convert a single string or number like x = int(x_str),y = int(y_str)
'''

# x,y = int(input("Enter number1 and number2: ").split(","))
# print("Sum:",x+y) 

# num1 = input("Enter number1: ")
# num2 = input("Enter number2: ")
# num1_int = int(num1)
# num2_int = int(num2)
# # print("Sum:",num1_int+num2_int)

# # #WE CAN WRITE USING f-string format in print() for output

# print(f"Sum:{num1_int + num2_int}")


#FINDING THE ARE OF A CIRCLE
#sample input:5, Expected output: 78.53981633974483
# FORMULA IS - "πr²"(r = radius)

'''radius = int(input("enter the circle radius: "))
area = 3.14*(radius**2)
print("Area of circle:",area,sep = "")
print(f"Area of circle:{3.14 * radius ** 2}",sep = "")
print(f"Area of circle:{area}") 
'''
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#QUADRATIC EQUATIONS - EXAMPLE 1
#Sample input a=1,b=-3,c=2 -#Expected output- Roots:(2.0,1.0)

#FORMULA IS: (-b ± √(b² - 4ac)) / (2a)

'''a = int(input("Give a value: "))
b = int(input("Give b value: "))
c = int(input("Give c value: "))
#Here we are dividing the formula first
#d = √(b² - 4ac)) / (2a) -first we define this
#we stored this (b² - 4ac) in d,then it will be √d, √d => d¹ᐟ² means d ** 0.5

root1 = (-b + (d**(0.5))) / 2*a
root2 =  (-b - (d**(0.5))) / 2*a
print(f"Roots:({root1},{root2})")
'''
#QUADRATIC EQUATIONS - EXAMPLE 2
#Sample input a=2,b=-2,c=3

#FORMULA IS: (-b ± √(b² - 4ac)) / (2a)
a = int(input("Give the value of a: "))
b = int(input("Give the value of b: "))
c = int(input("Give the value of c: "))
d = (b**2) - 4*a*c 
#we stored this (b² - 4ac) in d,then it will be √d, √d= d¹ᐟ² means d ** 0.5
root1 = (-b + (d**(0.5)))/2*a #using + Operator
root2 = (-b - (d**(0.5)))/2*a #using - Operator
print(f"Roots:({root1},{root2})")