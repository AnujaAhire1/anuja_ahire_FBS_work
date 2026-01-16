#WAP to Python Program to Find the Union of Two Lists

li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]
li = []

for i in li1:
    li.append(i)

for j in li2:
    found = False
    for k in li:
        if j == k:
            found = True
    if not found:
        li.append(j)

print("Union:", li)

