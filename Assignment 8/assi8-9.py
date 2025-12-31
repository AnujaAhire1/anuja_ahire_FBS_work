#WAP to Palindrome Number Check


def is_palindrome(num):
    return str(num) == str(num)[::-1]

n = int(input("Enter number: "))
print("Palindrome" if is_palindrome(n) else "Not Palindrome")




