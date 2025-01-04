# Constants
MONTHLY_LOSS = 4  # pounds per month
MONTHS = 6

# Get starting weight from user
starting_weight = float(input("Enter your starting weight (in pounds): "))

# Print header
print("\nMonth\tExpected Weight")
print("-" * 25)

# Initialize current weight
current_weight = starting_weight

# Loop through each month
for month in range(1, MONTHS + 1):
    # Calculate new weight
    current_weight -= MONTHLY_LOSS
    
    # Display results
    print(f"{month}\t{current_weight:.1f} lbs") 