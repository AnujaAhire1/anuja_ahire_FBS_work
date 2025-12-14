#WAP to swap two numbers without using third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping without third variable
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)