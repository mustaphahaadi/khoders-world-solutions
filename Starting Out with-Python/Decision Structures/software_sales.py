# Constants
PACKAGE_PRICE = 99

# Get number of packages from user
quantity = int(input("Enter the number of packages purchased: "))

# Determine discount rate based on quantity
if quantity < 0:
    print("Error: Quantity cannot be negative")
else:
    if quantity < 10:
        discount_rate = 0
    elif quantity < 20:
        discount_rate = 0.10  # 10%
    elif quantity < 50:
        discount_rate = 0.20  # 20%
    elif quantity < 100:
        discount_rate = 0.30  # 30%
    else:
        discount_rate = 0.40  # 40%

    # Calculate costs
    subtotal = quantity * PACKAGE_PRICE
    discount_amount = subtotal * discount_rate
    total = subtotal - discount_amount

    # Display results
    print(f"\nQuantity: {quantity}")
    print(f"Subtotal: ${subtotal:,.2f}")
    print(f"Discount: ${discount_amount:,.2f} ({discount_rate*100:.0f}%)")
    print(f"Total: ${total:,.2f}") 