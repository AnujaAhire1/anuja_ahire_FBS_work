#WAP  to find the area and circumference of circle

import math

# Taking input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculating area and circumference
area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
