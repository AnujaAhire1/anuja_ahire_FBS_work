#WAP to input angles of a triangle and check whether the triangle is valid or not.

a = float(input('Enter angle 1: '))
b = float(input('Enter angle 2: '))
c = float(input('Enter angle 3: '))

if a+b+c == 180:
    print('Triangle is valid.')
else:
    print('Triangle is Invalid.')