#WAP to Python Program to Sort the List According to the Second Element in Sublist

li = [[1, 3], [4, 1], [2, 2]]

n = len(li)
for i in range(n):
    for j in range(0, n - i - 1):
        if li[j][1] > li[j + 1][1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

print("Sorted list:", li)
