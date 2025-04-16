def convert_km_to_miles(kilometers):
    """Convert a distance in kilometers to miles using the formula: Miles = Kilometers * 0.6214"""
    miles = kilometers * 0.6214
    return miles

def main():
    # Get input from user
    try:
        kilometers = float(input("Enter a distance in kilometers: "))
        
        # Convert kilometers to miles
        miles = convert_km_to_miles(kilometers)
        
        # Display the result
        print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()