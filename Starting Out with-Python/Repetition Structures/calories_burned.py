# Constants
CALORIES_PER_MINUTE = 4.2

# Loop through different time intervals
for minutes in range(10, 31, 5):
    # Calculate calories burned
    calories = CALORIES_PER_MINUTE * minutes
    
    # Display results
    print(f"Calories burned after {minutes} minutes: {calories}") 