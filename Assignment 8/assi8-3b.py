#WAP to Sum of series: 1! + 2! + 3! + … + n!
def factorial_sum(n):
    fact = 1
    total = 0
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total

n = int(input("Enter n: "))
print("Sum of factorials:", factorial_sum(n))

