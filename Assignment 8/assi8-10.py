#WAP to Leap Year Check
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

y = int(input("Enter year: "))
print("Leap Year" if is_leap_year(y) else "Not a Leap Year")
