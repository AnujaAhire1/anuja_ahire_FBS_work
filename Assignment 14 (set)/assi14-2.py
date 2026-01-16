#WAP to Remove the intersection of a second set with a first set

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}

for i in s2:
    if i in s1:
        s1.remove(i)

print("After removing intersection:", s1)
