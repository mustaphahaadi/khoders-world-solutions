def calculate_county_sales_tax(total_sales):
    """Calculate the county sales tax (2.5% of total sales)"""
    return total_sales * 0.025

def calculate_state_sales_tax(total_sales):
    """Calculate the state sales tax (5% of total sales)"""
    return total_sales * 0.05

def calculate_total_sales_tax(total_sales):
    """Calculate the total sales tax (county + state)"""
    county_tax = calculate_county_sales_tax(total_sales)
    state_tax = calculate_state_sales_tax(total_sales)
    return county_tax + state_tax

def main():
    try:
        # Get total sales from user
        total_sales = float(input("Enter the total sales for the month: $"))
        
        # Validate input
        if total_sales < 0:
            print("Error: Sales amount cannot be negative.")
            return
            
        # Calculate taxes
        county_tax = calculate_county_sales_tax(total_sales)
        state_tax = calculate_state_sales_tax(total_sales)
        total_tax = calculate_total_sales_tax(total_sales)
        
        # Display results
        print(f"\nTotal sales: ${total_sales:.2f}")
        print(f"County sales tax (2.5%): ${county_tax:.2f}")
        print(f"State sales tax (5%): ${state_tax:.2f}")
        print(f"Total sales tax: ${total_tax:.2f}")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()