def feet_to_inches(feet):
    """Convert feet to inches (1 foot = 12 inches)"""
    return feet * 12

def main():
    try:
        # Get feet from user
        feet = float(input("Enter a number of feet: "))
        
        # Convert feet to inches
        inches = feet_to_inches(feet)
        
        # Display result
        print(f"{feet} feet equals {inches} inches.")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()