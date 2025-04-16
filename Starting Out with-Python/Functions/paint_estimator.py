def calculate_gallons_needed(square_feet):
    """Calculate gallons of paint needed (1 gallon per 112 square feet)"""
    return square_feet / 112

def calculate_labor_hours(square_feet):
    """Calculate labor hours needed (8 hours per 112 square feet)"""
    return (square_feet / 112) * 8

def calculate_paint_cost(gallons, price_per_gallon):
    """Calculate the cost of paint"""
    return gallons * price_per_gallon

def calculate_labor_cost(hours, hourly_rate=35):
    """Calculate the labor cost at $35 per hour"""
    return hours * hourly_rate

def main():
    # Constants
    LABOR_RATE = 35.00  # $35 per hour
    
    try:
        # Get input from user
        square_feet = float(input("Enter the square feet of wall space to be painted: "))
        paint_price = float(input("Enter the price of paint per gallon: $"))
        
        # Validate input
        if square_feet <= 0 or paint_price < 0:
            print("Error: Square feet must be positive and paint price cannot be negative.")
            return
            
        # Calculate all required values
        gallons_needed = calculate_gallons_needed(square_feet)
        labor_hours = calculate_labor_hours(square_feet)
        paint_cost = calculate_paint_cost(gallons_needed, paint_price)
        labor_cost = calculate_labor_cost(labor_hours, LABOR_RATE)
        total_cost = paint_cost + labor_cost
        
        # Display results
        print("\nPaint Job Estimate:")
        print(f"Wall space to be painted: {square_feet:.1f} square feet")
        print(f"Paint price: ${paint_price:.2f} per gallon")
        print(f"Number of gallons needed: {gallons_needed:.2f}")
        print(f"Hours of labor required: {labor_hours:.1f}")
        print(f"Cost of paint: ${paint_cost:.2f}")
        print(f"Labor charges: ${labor_cost:.2f}")
        print(f"Total cost of the paint job: ${total_cost:.2f}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()