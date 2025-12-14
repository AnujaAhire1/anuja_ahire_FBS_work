

for i in range(5):
    print(" " * (5 - i), end="")
    print("*", end="")
    if i > 0:
        print(" " * (2*i - 1) + "*")
    else:
        print()

for i in range(5-2, -1, -1):
    print(" " * (5 - i), end="")
    print("*", end="")
    if i > 0:
        print(" " * (2*i - 1) + "*")
    else:
        print()
