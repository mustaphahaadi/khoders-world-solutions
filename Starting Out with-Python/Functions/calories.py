def calculate_fat_calories(fat_grams):
    """Calculate calories from fat using the formula: calories = fat grams × 9"""
    return fat_grams * 9

def calculate_carb_calories(carb_grams):
    """Calculate calories from carbohydrates using the formula: calories = carb grams × 4"""
    return carb_grams * 4

def main():
    try:
        # Get input from user
        fat_grams = float(input("Enter the number of fat grams consumed: "))
        carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))
        
        # Validate input
        if fat_grams < 0 or carb_grams < 0:
            print("Error: Grams cannot be negative.")
            return
            
        # Calculate calories
        fat_calories = calculate_fat_calories(fat_grams)
        carb_calories = calculate_carb_calories(carb_grams)
        total_calories = fat_calories + carb_calories
        
        # Display results
        print(f"\nCalories from fat: {fat_calories:.1f}")
        print(f"Calories from carbohydrates: {carb_calories:.1f}")
        print(f"Total calories: {total_calories:.1f}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()