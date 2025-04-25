
## QUESTION 1
import random

# Generate a seven-digit lottery number
lottery_number = []
for i in range(7):
    lottery_number.append(random.randint(0, 9))

# Display the contents of the list
for number in lottery_number:
    print(number, end=' ') #end=' ' adds space between the numbers



## QUESTION 3
def falling_distance(t):
    g = 9.8
    d = 0.5 * g * t**2
    return d

# Call the function in a loop
for i in range(1, 11):
    distance = falling_distance(i)
    print(f"The distance fallen in {i} seconds is {distance} meters.")




# QUESTION 4
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





# QUESTION 2
def feet_to_inches(feet):
    inches = feet * 12
    return inches

# Use the function in a program
feet = float(input("Enter a number in feet: "))
inches = feet_to_inches(feet)
print(f"{feet} feet is equal to {inches} inches.")