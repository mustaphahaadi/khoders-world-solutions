# Get dimensions for first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# Get dimensions for second rectangle
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# Calculate areas
area1 = length1 * width1
area2 = length2 * width2

# Compare areas and display result
if area1 > area2:
    print("The first rectangle has a greater area")
elif area2 > area1:
    print("The second rectangle has a greater area")
else:
    print("Both rectangles have the same area")
