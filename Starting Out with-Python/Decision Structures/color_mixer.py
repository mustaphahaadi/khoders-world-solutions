# Get input of two primary colors
color1 = input("Enter first primary color (red, blue, or yellow): ").lower()
color2 = input("Enter second primary color (red, blue, or yellow): ").lower()

# Check if inputs are valid primary colors
valid_colors = ["red", "blue", "yellow"]
if color1 not in valid_colors or color2 not in valid_colors:
    print("Error: Please enter only red, blue, or yellow")
elif color1 == color2:
    print("Error: Please enter two different colors")
else:
    # Determine the secondary color
    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        print("When you mix red and blue, you get purple")
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        print("When you mix red and yellow, you get orange")
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        print("When you mix blue and yellow, you get green") 