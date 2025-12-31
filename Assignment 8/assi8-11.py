#WAP to Armstrong Number Check
def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10

    return total == num

n = int(input("Enter number: "))
print("Armstrong Number" if is_armstrong(n) else "Not an Armstrong Number")
