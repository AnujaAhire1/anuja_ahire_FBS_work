year = int(input("Enter a year: "))

if year % 4 == 0:                 # Step 1: divisible by 4?
    if year % 100 == 0:           # Step 2: divisible by 100?
        if year % 400 == 0:       # Step 3: divisible by 400?
            print("Leap Year")
        else:
            print("NOT a Leap Year")
    else:
        print("Leap Year")
else:
    print("NOT a Leap Year")

