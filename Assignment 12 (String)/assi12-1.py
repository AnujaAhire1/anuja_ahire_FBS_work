#WAP to Python Program to Replace all Occurrences of ‘a’ with $ in a String

s = "banana"
result = ""

for ch in s:
    if ch == 'a':
        result = result + '$'
    else:
        result = result + ch

print(result)
