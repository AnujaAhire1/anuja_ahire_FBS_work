#WAP to except an integer amount from the user and tell minimum number of notes needed for representing that amount

amount = int(input("Enter the amount: "))

# Available denominations
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("\nMinimum number of notes:")

count = 0
for note in notes:
    if amount >= note:
        num = amount // note
        print(f"₹{note} : {num} notes")
        count += num
        amount = amount % note

print("\nTotal notes needed:", count)
