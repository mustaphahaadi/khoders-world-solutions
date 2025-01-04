# Get number of years from user
years = int(input("Enter the number of years: "))

# Initialize variables
total_months = years * 12
total_rainfall = 0

# Outer loop for years
for year in range(1, years + 1):
    print(f"\nYear {year}")
    # Inner loop for months
    for month in range(1, 13):
        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
        total_rainfall += rainfall

# Calculate average
average_rainfall = total_rainfall / total_months

# Display results
print("\n=== Rainfall Statistics ===")
print(f"Number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches") 