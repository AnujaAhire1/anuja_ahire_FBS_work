

for i in range(1, 5+1):
    print("  " * (5 - i), end="")
    ch = ord('A')
    for j in range(2*i - 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
