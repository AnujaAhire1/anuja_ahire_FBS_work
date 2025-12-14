#WAP to input two angles from user and find third angle of the triangle.

#Taking input from the user
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))

# Calculating third angle
third_angle = 180 - (angle1 + angle2)

print("The third angle of the triangle is:", third_angle)