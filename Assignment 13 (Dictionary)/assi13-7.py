#WAP to Python Program to Remove the Given Key from a Dictionary

d = {1: "apple", 2: "banana", 3: "cherry"}
key = int(input("Enter key to remove: "))

if key in d:
    del d[key]

print("Updated Dictionary:", d)
 