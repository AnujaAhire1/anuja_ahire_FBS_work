#WAP to Find missing numbers in second set compared to first and vice versa

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

missing_in_s2 = set()
missing_in_s1 = set()

for i in s1:
    if i not in s2:
        missing_in_s2.add(i)

for j in s2:
    if j not in s1:
        missing_in_s1.add(j)

print("Missing in second set:", missing_in_s2)
print("Missing in first set:", missing_in_s1)
