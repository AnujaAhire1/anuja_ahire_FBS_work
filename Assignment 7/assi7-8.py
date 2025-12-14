
for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(2 * (5 - i) - 1):
        print(" ", end=" ")

    if i == 5:
        for j in range(4, 0, -1):
            print(j, end=" ")
    else:
        for j in range(i, 0, -1):
            print(j, end=" ")

    print()
