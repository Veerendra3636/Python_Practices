# SWAPPING TWO VALUES WITH USING TEMPORARY VARIABLE
# input values: a = 10, b = 20
# output values: a = 20, b = 10

'''
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
temp = a #here we are storing a value in temp variable now temp = 10
a = b #here we are storing b value into a so now a = 20
b = temp
print(f"Result of a: {a}")
print(f"Result of b: {b}")
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# SWAPPING TWO VALUES WITHOUT USING TEMPORARY VARIABLE
# input values: a = 10, b = 20
# output values: a = 20, b = 10

# a = int(input("Enter value a :"))
# b = int(input("Enter value b :"))

# a = a+b #now a value is 30, b value is still 20
# b = a-b
# a = a-b
# print(f"Result of a: {a}")
# print(f"Result of a: {b}")

# SWAPPING TWO VALUES WITHOUT USING TEMPORARY VARIABLE -EXAMPLE 2
# input values: x = 20, y = 30


# x = int(input("Enter x value: "))
# y = int(input("Enter y value: "))

# x = x+y #50
# y = x-y #20
# x = x-y #30
# print(f"Value of x:{x}")
# print(f"Value of y:{y}")

# SWAPPING TWO VALUES WITHOUT USING TEMPORARY VARIABLE
# input values: p = 30, q = 10

p = int(input("Enter p value: "))
q = int(input("Enter q value: "))

p = p+q #40
q = p-q #30
p = p-q

print(f"Value of p:{p}")
print(f"Value of q:{q}")