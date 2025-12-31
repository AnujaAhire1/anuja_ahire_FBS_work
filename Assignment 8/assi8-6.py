#WAP to Fibonacci Series (n terms)
def fibonacci(n):
    a, b = 1, 1
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)
