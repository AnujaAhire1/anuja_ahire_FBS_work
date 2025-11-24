#WAP to calculate area of an equilateral traingle

import math

# Taking input from the user
side = float(input("Enter the side of the equilateral triangle: "))

# Calculating area
area = (math.sqrt(3) / 4) * side * side

print("The area of the equilateral triangle is:", area)