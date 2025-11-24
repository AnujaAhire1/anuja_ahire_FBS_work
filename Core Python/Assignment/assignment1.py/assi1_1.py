# WAP to calculate percentage of a student based on marks of any 5 subjects

# Taking input for 5 subjects
s1 = float(input("Enter marks of Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
s4 = float(input("Enter marks of Subject 4: "))
s5 = float(input("Enter marks of Subject 5: "))

# Calculate total marks
total = s1 + s2 + s3 + s4 + s5

# Calculate percentage
percentage = (total / 500) * 100

print (percentage)