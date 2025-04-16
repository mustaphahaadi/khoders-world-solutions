def calculate_county_tax(purchase_amount):
    """Calculate the county sales tax (2% of the purchase amount)"""
    return purchase_amount * 0.02

def calculate_state_tax(purchase_amount):
    """Calculate the state sales tax (4% of the purchase amount)"""
    return purchase_amount * 0.04

def calculate_total_tax(purchase_amount):
    """Calculate the total sales tax (county + state)"""
    county_tax = calculate_county_tax(purchase_amount)
    state_tax = calculate_state_tax(purchase_amount)
    return county_tax + state_tax

def calculate_total_sale(purchase_amount):
    """Calculate the total of the sale (purchase amount + total tax)"""
    total_tax = calculate_total_tax(purchase_amount)
    return purchase_amount + total_tax

def display_tax_info(purchase_amount):
    """Display all tax information and totals"""
    county_tax = calculate_county_tax(purchase_amount)
    state_tax = calculate_state_tax(purchase_amount)
    total_tax = calculate_total_tax(purchase_amount)
    total_sale = calculate_total_sale(purchase_amount)
    
    print(f"Purchase Amount: ${purchase_amount:.2f}")
    print(f"County Sales Tax (2%): ${county_tax:.2f}")
    print(f"State Sales Tax (4%): ${state_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")
    print(f"Total Sale Amount: ${total_sale:.2f}")

def main():
    # Get the purchase amount from the user
    try:
        purchase_amount = float(input("Enter the purchase amount: $"))
        if purchase_amount < 0:
            print("Error: Purchase amount cannot be negative.")
            return
            
        # Display all tax information
        display_tax_info(purchase_amount)
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()