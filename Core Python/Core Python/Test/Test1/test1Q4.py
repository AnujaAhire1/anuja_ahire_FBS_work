#WAP to calculate the cost of painting the following building's walls

# Taking input from the user
area = float(input("Enter area of one wall: "))
cost_interior = float(input("Enter cost of interior painting per sq.ft: "))
cost_exterior = float(input("Enter cost of exterior painting per sq.ft: "))

# Two rooms = 4 walls each = 8 walls total
total_area = area * 8

interior_cost = total_area * cost_interior
exterior_cost = total_area * cost_exterior

print("Total interior painting cost =", interior_cost)
print("Total exterior painting cost =", exterior_cost)
print("Total painting cost =", interior_cost + exterior_cost)