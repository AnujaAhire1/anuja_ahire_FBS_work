#WAP to convert distant given in feet and inches into meter and centimeter

 #Taking input
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

# Converting feet and inches to total inches
total_inches = feet * 12 + inches

# 1 inch = 2.54 cm
centimeters = total_inches * 2.54

# Convert cm to meters and centimeters
meters = int(centimeters // 100)
remaining_cm = centimeters % 100

print("Distance in meters and centimeters:")
print("Meters:", meters)
print("Centimeters:", remaining_cm)
