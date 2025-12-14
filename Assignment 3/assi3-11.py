total_amount = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    ticket = float(input(f"Enter ticket amount of person {i}: "))

    if age < 12:
        discount = ticket * 0.30
        payable = ticket - discount
    elif age > 59:
        discount = ticket * 0.50
        payable = ticket - discount
    else:
        payable = ticket

    total_amount += payable

print("Total ticket amount to be paid:", total_amount)
