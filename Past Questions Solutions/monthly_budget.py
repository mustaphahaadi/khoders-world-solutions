# Ask the user to enter the budget for the month
budget = float(input("Enter your budget for the month: "))

# Initialize the total expenses
total_expenses = 0

# Loop to enter each expense and keep a running total
while True:
    expense = input("Enter an expense (or 'done' to finish): ")
    if expense.lower() == 'done':
        break
    total_expenses += float(expense)

# Calculate the difference between the budget and the total expenses
difference = total_expenses - budget

# Display the result
if difference > 0:
    print(f"You are over budget by {difference:.2f}.")
elif difference < 0:
    print(f"You are under budget by {-difference:.2f}.")
else:
    print("You are exactly on budget.")
