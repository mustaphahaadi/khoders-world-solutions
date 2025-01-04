# Constants
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600  # 60 * 60
SECONDS_PER_DAY = 86400  # 24 * 60 * 60

# Get seconds from user
seconds = int(input("Enter the number of seconds: "))

if seconds < 0:
    print("Error: Please enter a positive number of seconds")
else:
    # Calculate time units
    days = seconds // SECONDS_PER_DAY
    seconds_remaining = seconds % SECONDS_PER_DAY
    
    hours = seconds_remaining // SECONDS_PER_HOUR
    seconds_remaining = seconds_remaining % SECONDS_PER_HOUR
    
    minutes = seconds_remaining // SECONDS_PER_MINUTE
    seconds_remaining = seconds_remaining % SECONDS_PER_MINUTE

    # Display results
    if seconds >= SECONDS_PER_DAY:
        print(f"{days} days, {hours} hours, {minutes} minutes, {seconds_remaining} seconds")
    elif seconds >= SECONDS_PER_HOUR:
        print(f"{hours} hours, {minutes} minutes, {seconds_remaining} seconds")
    elif seconds >= SECONDS_PER_MINUTE:
        print(f"{minutes} minutes, {seconds_remaining} seconds")
    else:
        print(f"{seconds} seconds") 