#WAP Remove duplicates from list

li= [1, 2, 2, 3, 4, 3]
new_li= []

for i in li:
    found = False
    for j in new_li:
        if i == j:
            found = True
    if not found:
        new_li.append(i)

print("List without duplicates:", new_li)
