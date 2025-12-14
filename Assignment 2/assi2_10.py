#WAP to reverse three-digit number

num = int(input("Enter a three-digit number: "))

# Extract digits
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

# Reverse number
reverse_num = ones * 100 + tens * 10 + hundreds

print("Reversed Number =", reverse_num)