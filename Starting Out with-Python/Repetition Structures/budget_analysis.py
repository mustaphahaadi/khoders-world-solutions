# Get the monthly budget from user
monthly_budget = float(input("Enter your monthly budget: $"))

# Initialize variables
total_expenses = 0
expense_count = 1

# Loop to get expenses
while True:
    # Get expense from user
    expense = float(input(f"\nEnter expense #{expense_count} (or 0 to finish): $"))
    
    # Check if user wants to finish
    if expense == 0:
        break
        
    # Add expense to total
    total_expenses += expense
    expense_count += 1

# Calculate difference from budget
difference = monthly_budget - total_expenses

# Display results
print("\n=== Budget Analysis ===")
print(f"Monthly Budget: ${monthly_budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
if difference > 0:
    print(f"You are under budget by ${difference:.2f}")
else:
    print(f"You are over budget by ${abs(difference):.2f}") 