def calculate_minimum_insurance(replacement_cost):
    """Calculate the minimum insurance amount (80% of replacement cost)"""
    return replacement_cost * 0.8

def main():
    # Get the replacement cost from the user
    try:
        replacement_cost = float(input("Enter the replacement cost of the building: $"))
        if replacement_cost < 0:
            print("Error: Replacement cost cannot be negative.")
            return
            
        # Calculate and display the minimum insurance amount
        min_insurance = calculate_minimum_insurance(replacement_cost)
        print(f"Replacement cost: ${replacement_cost:.2f}")
        print(f"Minimum insurance recommended: ${min_insurance:.2f}")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()