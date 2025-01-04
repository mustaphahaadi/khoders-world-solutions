# Initialize the total bugs variable
total_bugs = 0

# Loop for 5 days
for day in range(1, 6):
    # Get input from user for each day
    bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
    
    # Add bugs to running total
    total_bugs += bugs

# Display the final total
print(f"\nTotal bugs collected over 5 days: {total_bugs}") 