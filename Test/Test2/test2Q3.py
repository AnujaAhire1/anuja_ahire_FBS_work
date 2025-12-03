import math

r = 20
length = 50
breadth = 40
wire_cost = 35
rounds = 5

# Perimeter = half circle + rectangle sides
perimeter = (math.pi * r) + length + (2 * breadth)

total_wire_length = perimeter * rounds
total_cost = total_wire_length * wire_cost

print("Total cost of fencing =", round(total_cost, 2), "Rs")
