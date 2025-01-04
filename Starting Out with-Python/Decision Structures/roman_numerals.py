# Get input from user
number = int(input("Enter a number (1-10): "))

# Convert number to Roman numeral using if-elif statements
if number == 1:
    roman = "I"
elif number == 2:
    roman = "II"
elif number == 3:
    roman = "III"
elif number == 4:
    roman = "IV"
elif number == 5:
    roman = "V"
elif number == 6:
    roman = "VI"
elif number == 7:
    roman = "VII"
elif number == 8:
    roman = "VIII"
elif number == 9:
    roman = "IX"
elif number == 10:
    roman = "X"
else:
    roman = "Error: Please enter a number between 1 and 10"

# Display result
print(f"Roman numeral: {roman}") 