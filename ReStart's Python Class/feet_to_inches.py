def feet_to_inches(feet):
    inches = feet * 12
    return inches

# Use the function in a program
feet = float(input("Enter a number in feet: "))
inches = feet_to_inches(feet)
print(f"{feet} feet is equal to {inches} inches.")