#WAP to enter P, T, R and calculate Simple Interest.

#Taking input from  the user
P = float(input("Enter the Principal amount: "))
T = float(input("Enter the Time in years: "))
R = float(input("Enter the Rate of interest: "))

# Calculating Simple Interest
SI = (P * T * R) / 100

print("Simple Interest =", SI)