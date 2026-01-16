#WAP to Check element presence and count

li = [1, 2, 3, 2, 4, 2]
num = int(input("Enter number: "))

count = 0
for i in li:
    if i == num:
        count = count + 1

if count > 0:
    print(num, "is present", count, "times")
else:
    print(num, "is not present")
