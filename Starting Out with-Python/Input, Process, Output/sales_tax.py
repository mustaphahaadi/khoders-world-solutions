# Get purchase amount from user
purchase_amount = float(input("Enter the purchase amount: $"))

# Calculate taxes
state_tax = purchase_amount * 0.05
county_tax = purchase_amount * 0.025
total_tax = state_tax + county_tax
total_sale = purchase_amount + total_tax

# Display results
print(f"\nPurchase amount: ${purchase_amount:.2f}")
print(f"State sales tax: ${state_tax:.2f}")
print(f"County sales tax: ${county_tax:.2f}")
print(f"Total sales tax: ${total_tax:.2f}")
print(f"Total sale: ${total_sale:.2f}") 