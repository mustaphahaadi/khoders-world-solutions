# Get number of days from user
days = int(input("Enter the number of days: "))

# Initialize variables
total_pay = 0
daily_pay = 1  # Start with one penny

# Print header
print("\nDay\tSalary")
print("-" * 20)

# Loop through each day
for day in range(1, days + 1):
    # Display daily pay in dollars
    print(f"{day}\t${daily_pay/100:.2f}")
    
    # Add to total
    total_pay += daily_pay
    
    # Double the pay for next day
    daily_pay *= 2

# Display total
print("\nTotal pay: ${:.2f}".format(total_pay/100)) 