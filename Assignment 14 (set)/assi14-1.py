#WAP to Find elements in a given set that are not in another set

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 6}

result = set()

for i in s1:
    if i not in s2:
        result.add(i)

print("Elements in s1 but not in s2:", result)

