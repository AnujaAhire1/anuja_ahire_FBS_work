#WAP to Second largest element in a list

li = [10, 20, 5, 30, 25]

largest = li[0]
second = li[0]

for i in li:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest =", second)
