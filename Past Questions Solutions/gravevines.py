# Get input from user
row_length = float(input("Enter the length of the row (in feet): "))
end_post_space = float(input("Enter the space used by end-post assembly (in feet): "))
vine_spacing = float(input("Enter the space between vines (in feet): "))

# Calculate number of grapevines
# Formula: V = (R - 2E) / S
number_of_vines = (row_length - 2 * end_post_space) / vine_spacing

# Display result
print("Number of grapevines that will fit in the row", number_of_vines, "vines.")