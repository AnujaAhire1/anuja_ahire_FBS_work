#WAP to find quotient and reminder of two numbers.

# Taking input from the user
num1 = int(input("Enter the dividend (number to be divided): "))
num2 = int(input("Enter the divisor (number to divide by): "))

# Calculating quotient and remainder
quotient = num1 // num2
remainder = num1 % num2

print("Quotient:", quotient)
print("Remainder:", remainder)