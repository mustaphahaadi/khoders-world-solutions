# Get input from user
day_number = int(input("Enter a number (1-7): "))

# Check if number is in valid range and display corresponding day
if 1 <= day_number <= 7:
    if day_number == 1:
        print("Monday")
    elif day_number == 2:
        print("Tuesday")
    elif day_number == 3:
        print("Wednesday")
    elif day_number == 4:
        print("Thursday")
    elif day_number == 5:
        print("Friday")
    elif day_number == 6:
        print("Saturday")
    else:
        print("Sunday")
else:
    print("Error: Please enter a number between 1 and 7")