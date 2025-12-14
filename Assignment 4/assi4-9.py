#WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
div = int(input("Enter the number to divide by: "))

print("Numbers divisible by", div, "are:")

for i in range(start, end + 1):
    if i % div == 0:
        print(i)

