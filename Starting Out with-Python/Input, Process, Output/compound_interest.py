# Get input from user
principal = float(input("Enter the principal amount: $"))
annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
compounds_per_year = float(input("Enter number of times interest is compounded per year: "))
years = float(input("Enter number of years: "))

# Convert interest rate from percentage to decimal
rate = annual_rate / 100

# Calculate final amount using compound interest formula
# A = P(1 + r/n)^(nt)
final_amount = principal * (1 + rate/compounds_per_year)**(compounds_per_year * years)

# Display result
print(f"\nAfter {years} years, the account will be worth: ${final_amount:,.2f}") 