# Get prices for all 5 items
item1 = float(input("Enter price of item 1: $"))
item2 = float(input("Enter price of item 2: $"))
item3 = float(input("Enter price of item 3: $"))
item4 = float(input("Enter price of item 4: $"))
item5 = float(input("Enter price of item 5: $"))

# Calculate subtotal
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate tax and total
tax = subtotal * 0.07
total = subtotal + tax

# Display results
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}") 