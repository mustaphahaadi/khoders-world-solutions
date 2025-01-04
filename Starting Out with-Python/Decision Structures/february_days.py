# Get year from user
year = int(input("Enter a year: "))

# Determine if it's a leap year
if year <= 0:
    print("Error: Please enter a valid year")
else:
    # Check if year is divisible by 100
    if year % 100 == 0:
        # If divisible by 100, must also be divisible by 400 to be leap year
        is_leap_year = year % 400 == 0
    else:
        # If not divisible by 100, must be divisible by 4 to be leap year
        is_leap_year = year % 4 == 0

    # Determine days in February
    if is_leap_year:
        days = 29
    else:
        days = 28

    # Display result
    print(f"In {year} February has {days} days.") 