
for i in range(1, 5):
    print("1", end="")
    if i > 1:
        print(" " * (2*i-3) + str(i))
    else:
        print()

for j in range(1, 5+1):
    print(j, end=" ")
