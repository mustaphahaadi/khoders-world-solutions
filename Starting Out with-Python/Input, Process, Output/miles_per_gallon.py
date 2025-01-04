# Get input from user
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the gallons of gas used: "))

# Calculate MPG
mpg = miles_driven / gallons_used

# Display result
print(f"\nMiles per gallon: {mpg:.2f}")