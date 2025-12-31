#WAP to Reverse of a Number
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = int(input("Enter number: "))
print("Reverse:", reverse_number(n))

