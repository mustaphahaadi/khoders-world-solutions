def calculate_assessment_value(actual_value):
    """Calculate the assessment value (60% of actual value)"""
    return actual_value * 0.6

def calculate_property_tax(assessment_value):
    """Calculate the property tax ($0.72 for each $100 of assessment value)"""
    return (assessment_value / 100) * 0.72

def main():
    try:
        # Get the actual property value from the user
        actual_value = float(input("Enter the actual value of the property: $"))
        if actual_value < 0:
            print("Error: Property value cannot be negative.")
            return
            
        # Calculate assessment value and property tax
        assessment_value = calculate_assessment_value(actual_value)
        property_tax = calculate_property_tax(assessment_value)
        
        # Display results
        print(f"\nActual Property Value: ${actual_value:.2f}")
        print(f"Assessment Value: ${assessment_value:.2f}")
        print(f"Property Tax: ${property_tax:.2f}")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()