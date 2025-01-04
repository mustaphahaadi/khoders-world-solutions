# Get number of books purchased from user
books = int(input("Enter the number of books purchased this month: "))

# Determine points based on books purchased
if books < 0:
    print("Error: Number of books cannot be negative")
elif books < 2:
    points = 0
elif books < 4:
    points = 5
elif books < 6:
    points = 15
elif books < 8:
    points = 30
else:  # 8 or more books
    points = 60

# Display points earned
if books >= 0:
    print(f"You have earned {points} points!") 