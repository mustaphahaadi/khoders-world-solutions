# Get package weight from user
weight = float(input("Enter the weight of the package in pounds: "))

# Determine shipping rate based on weight
if weight <= 0:
    print("Error: Weight must be greater than 0")
else:
    if weight <= 2:
        rate = 1.50
    elif weight <= 6:
        rate = 3.00
    elif weight <= 10:
        rate = 4.00
    else:
        rate = 4.75

    # Calculate and display shipping charges
    charges = weight * rate
    print(f"\nWeight: {weight:.2f} pounds")
    print(f"Rate per pound: ${rate:.2f}")
    print(f"Shipping charges: ${charges:.2f}") 