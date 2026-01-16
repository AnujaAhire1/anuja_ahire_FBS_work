#WAP to Remove all occurrences of a given element

li = [1, 2, 3, 2, 4, 2]
num = int(input("Enter element to remove: "))
new_li = []

for i in li:
    if i != num:
        new_li.append(i)

print("Updated list:", new_li)
