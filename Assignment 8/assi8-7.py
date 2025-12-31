#WAP to Sum of Digits of a Number
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

n = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(n))
