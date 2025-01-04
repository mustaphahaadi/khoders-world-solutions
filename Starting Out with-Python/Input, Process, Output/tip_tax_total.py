# Get food charge from user
food_charge = float(input("Enter the charge for food: $"))

# Calculate tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Display results
print(f"\nFood Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}") 