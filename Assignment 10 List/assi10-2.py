#WAP to Find maximum and minimum element in a list

li = [10, 5, 30, 2, 50]

max_val = li[0]
min_val = li[0]

for i in li:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum =", max_val)
print("Minimum =", min_val)
