# Get date input from user
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
year = int(input("Enter the two-digit year (00-99): "))

# Check if date is magic
if month * day == year:
    print(f"{month}/{day}/{year:02d} is a magic date!")
else:
    print(f"{month}/{day}/{year:02d} is not a magic date") 