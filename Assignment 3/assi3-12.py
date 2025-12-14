#WAP Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))

# Check whether number is 3-digit
if num >= 100 and num <= 999:
    original = num

    # Reverse the number
    rev = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    # Check palindrome
    if original == rev:
        print("The number is a Palindrome")
    else:
        print("The number is Not a Palindrome")
else:
    print("Please enter a valid 3-digit number")

