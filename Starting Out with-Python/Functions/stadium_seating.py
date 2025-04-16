def calculate_class_income(num_tickets, ticket_price):
    """Calculate income from a specific seating class"""
    return num_tickets * ticket_price

def main():
    # Ticket prices for each class
    CLASS_A_PRICE = 20
    CLASS_B_PRICE = 15
    CLASS_C_PRICE = 10
    
    try:
        # Get number of tickets sold for each class
        class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
        class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
        class_c_tickets = int(input("Enter the number of Class C tickets sold: "))
        
        # Validate input
        if class_a_tickets < 0 or class_b_tickets < 0 or class_c_tickets < 0:
            print("Error: Number of tickets cannot be negative.")
            return
            
        # Calculate income for each class
        class_a_income = calculate_class_income(class_a_tickets, CLASS_A_PRICE)
        class_b_income = calculate_class_income(class_b_tickets, CLASS_B_PRICE)
        class_c_income = calculate_class_income(class_c_tickets, CLASS_C_PRICE)
        
        # Calculate total income
        total_income = class_a_income + class_b_income + class_c_income
        
        # Display results
        print("\nIncome from ticket sales:")
        print(f"Class A (${CLASS_A_PRICE} each): ${class_a_income:.2f}")
        print(f"Class B (${CLASS_B_PRICE} each): ${class_b_income:.2f}")
        print(f"Class C (${CLASS_C_PRICE} each): ${class_c_income:.2f}")
        print(f"Total income: ${total_income:.2f}")
    except ValueError:
        print("Error: Please enter valid whole numbers for ticket quantities.")

if __name__ == "__main__":
    main()