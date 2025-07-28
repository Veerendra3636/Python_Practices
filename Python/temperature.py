#CONVERTING TEMPERATURE UNITS
# Sample input: temperature_celsius = 30

# OUTPUT EXPECTING IN Fahrenheit and Kelvin
#we should convert the values string to int or float

# temperature_celsius = float(input("Enter heat in celsius: "))

# '''converting celsius into fahrenheit
# FORMULA: F = celsius * (9/5) +32'''

# f = temperature_celsius * (9/5) + 32

# '''converting celsius into Kelvin 
# FORMULA: K = 273 + celsius'''
# k = 273 + temperature_celsius

# print(f"temperature in fahrenheit:{f}")
# print(f"temperature in kelvin:{k}")

'''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

'''
#BASIC CURRENCY CONVERTER

amount_in_usd = int(input("Enter amount in use: "))
#sample input amount_in_usd = 100
#formula is 
# 1usd = 0.85 euro
# 100usd = (eur * amt)
amount_in_euro = 0.85 * amount_in_usd
print(f"Amount in euro:{amount_in_euro}")
