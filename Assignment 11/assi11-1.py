#WAP to Python Program to Put Even and Odd elements of a List into two Different Lists

li = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even list:", even)
print("Odd list:", odd)
