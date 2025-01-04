# Get pocket number from user
pocket = int(input("Enter a pocket number (0-36): "))

# Check if number is valid
if pocket < 0 or pocket > 36:
    print("Error: Please enter a number between 0 and 36")
else:
    # Determine pocket color
    if pocket == 0:
        color = "green"
    elif 1 <= pocket <= 10:
        color = "red" if pocket % 2 == 1 else "black"
    elif 11 <= pocket <= 18:
        color = "black" if pocket % 2 == 1 else "red"
    elif 19 <= pocket <= 28:
        color = "red" if pocket % 2 == 1 else "black"
    else:  # 29-36
        color = "black" if pocket % 2 == 1 else "red"
    
    print(f"Pocket {pocket} is {color}") 