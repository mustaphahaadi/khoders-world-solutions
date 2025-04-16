def calculate_monthly_total(loan, insurance, gas, oil, tires, maintenance):
    """Calculate the total monthly automobile expenses"""
    return loan + insurance + gas + oil + tires + maintenance

def calculate_annual_total(monthly_total):
    """Calculate the total annual automobile expenses"""
    return monthly_total * 12

def main():
    try:
        # Get monthly costs from the user
        loan_payment = float(input("Enter monthly loan payment: $"))
        insurance = float(input("Enter monthly insurance cost: $"))
        gas = float(input("Enter monthly gas cost: $"))
        oil = float(input("Enter monthly oil cost: $"))
        tires = float(input("Enter monthly tires cost: $"))
        maintenance = float(input("Enter monthly maintenance cost: $"))
        
        # Calculate totals
        monthly_total = calculate_monthly_total(loan_payment, insurance, gas, oil, tires, maintenance)
        annual_total = calculate_annual_total(monthly_total)
        
        # Display results
        print("\nExpense Summary:")
        print(f"Monthly automobile expenses: ${monthly_total:.2f}")
        print(f"Annual automobile expenses: ${annual_total:.2f}")
    except ValueError:
        print("Error: Please enter valid numbers for all expenses.")

if __name__ == "__main__":
    main()