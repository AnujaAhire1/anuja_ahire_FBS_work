height = float(input("Enter height of the walls: "))
width = float(input("Enter width of the walls: "))
cost_per_sq_m = float(input("Enter painting cost per sq. meter: "))

area = 4 * height * width
total_cost = area * cost_per_sq_m

print("Total painting cost =", total_cost)
