# Constants
INITIAL_TUITION = 8000
INCREASE_RATE = 0.03
YEARS = 5

# Initialize tuition
tuition = INITIAL_TUITION

# Print header
print("Year\tTuition Amount")
print("-" * 25)

# Loop through each year
for year in range(1, YEARS + 1):
    print(f"{year}\t${tuition:,.2f}")
    # Calculate next year's tuition
    tuition = tuition * (1 + INCREASE_RATE) 