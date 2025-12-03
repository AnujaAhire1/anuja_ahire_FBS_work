total = 0

for i in range(5):
    price = float(input(f"Enter price of product {i+1}: "))
    total += price

gst = total * 0.18
bill = total + gst

print("Total bill after adding 18% GST =", bill)

