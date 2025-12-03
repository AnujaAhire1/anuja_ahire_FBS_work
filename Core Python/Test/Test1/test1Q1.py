#WAP to find the area and perimeter of following figure

#Taking input from the user

import math
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

# Area = rectangle + circle
area = (length * breadth) + (math.pi * radius**2)

# Perimeter
# Straight portion: 2*(length - 2*radius)
# Curved portion: full circle = 2*pi*r
perimeter = 2 * (length - 2 * radius) + 2 * math.pi * radius + 2 * radius

print("Area of figure =", area)
print("Perimeter of figure =", perimeter)