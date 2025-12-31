# 1) Sum of series: 1! + 2! + 3! + ... + n!

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def series_sum(n):
    if n == 1:
        return fact(1)
    return fact(n) + series_sum(n - 1)

n = int(input("Enter n: "))
print("Sum of series =", series_sum(n))

