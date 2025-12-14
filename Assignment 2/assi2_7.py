#WAP to find the sum of three digit number

num = int(input("Enter a three-digit number: "))

# Extract digits
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

# Sum of digits
total = hundreds + tens + ones

print("Sum of digits =", total)

