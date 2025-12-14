#WAP to convert temmp from Celesius to Fahrenheit (C/5=(F-32)/9)

celsius = float(input("Enter temperature in Celsius: "))

# Using the formula C/5 = (F - 32)/9
fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)