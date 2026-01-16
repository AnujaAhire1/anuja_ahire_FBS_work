#WAP to Find all unique combinations of 3 numbers adding up to a target number

li = [1, 2, 3, 4, 5, 6]
target = 10
combinations = set()

n = len(li)
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if li[i] + li[j] + li[k] == target:
                combinations.add((li[i], li[j], li[k]))

print("Unique combinations:", combinations)

