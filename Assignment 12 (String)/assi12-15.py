#WAP to Python Program to Find Larger String Without Using Built-in Function

s1 = "java"
s2 = "python"

c1 = 0
c2 = 0

for i in s1:
    c1 += 1
for j in s2:
    c2 += 1

if c1 > c2:
    print("Larger string:", s1)
else:
    print("Larger string:", s2)

