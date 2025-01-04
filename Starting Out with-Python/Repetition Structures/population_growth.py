# Get input from user
initial_organisms = float(input("Enter the starting number of organisms: "))
daily_increase = float(input("Enter the average daily increase (as a percentage): ")) / 100
days = int(input("Enter the number of days to multiply: "))

# Validate input
if initial_organisms < 0 or daily_increase < 0 or days < 0:
    print("Please enter positive values only.")
    exit()

# Print header
print("\nDay\tApproximate Population")
print("-" * 30)

# Initialize population
population = initial_organisms

# Loop through each day
for day in range(1, days + 1):
    # Display current population
    print(f"{day}\t{population:.6f}")
    
    # Calculate next day's population
    population = population + (population * daily_increase) 