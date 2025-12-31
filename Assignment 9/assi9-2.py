#WAP to Check Armstrong number 
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def armstrong(num, digits):
    if num == 0:
        return 0
    return power(num % 10, digits) + armstrong(num // 10, digits)

n = int(input("Enter number: "))
d = len(str(n))

if armstrong(n, d) == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
