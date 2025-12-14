#WAP Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = float(input("Enter mark1: "))
m2 = float(input("Enter mark2: "))
m3 = float(input("Enter mark3: "))
m4 = float(input("Enter mark4: "))
m5 = float(input("Enter mark5: "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

if avg >= 75:
    print("Distinction")
elif avg >= 60:
    print("First Class")
elif avg >= 50:
    print("Second Class")
elif avg >= 35:
    print("Pass Class")
else:
    print("Fail")
