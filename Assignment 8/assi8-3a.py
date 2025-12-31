#WAP to Sum of series: 1 + 2 + 3 + … + n
def sum_n(n):
    return n * (n + 1) // 2

n = int(input("Enter n: "))
print("Sum:", sum_n(n))

