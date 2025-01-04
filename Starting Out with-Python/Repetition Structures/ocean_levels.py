# Constants
ANNUAL_RISE = 1.6  # millimeters per year
YEARS = 25

# Print header
print("Year\tRise in mm")
print("-" * 20)

# Loop through each year
for year in range(1, YEARS + 1):
    # Calculate rise for current year
    total_rise = ANNUAL_RISE * year
    
    # Display results
    print(f"{year}\t{total_rise:.1f}") 