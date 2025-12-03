#WAp to calculate simple Interest based on Principle, Rate and Time

# Taking input from the User

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)