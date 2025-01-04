# Constants for coin values (in cents)
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
DOLLAR_VALUE = 100  # one dollar in cents

# Get input from user
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

# Calculate total in cents
total_cents = (pennies * PENNY_VALUE + 
               nickels * NICKEL_VALUE + 
               dimes * DIME_VALUE + 
               quarters * QUARTER_VALUE)

# Check if total equals one dollar
if total_cents == DOLLAR_VALUE:
    print("Congratulations! That equals exactly one dollar! You win!")
elif total_cents < DOLLAR_VALUE:
    print(f"Sorry, that's only {total_cents} cents. That's less than one dollar.")
else:
    print(f"Sorry, that's {total_cents} cents. That's more than one dollar.") 