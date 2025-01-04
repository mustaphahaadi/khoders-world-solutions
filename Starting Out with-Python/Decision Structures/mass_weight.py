# Get mass from user
mass = float(input("Enter the object's mass in kilograms: "))

# Calculate weight
weight = mass * 9.8

# Display the weight
print(f"The object's weight is {weight:.2f} newtons")

# Check if weight is too heavy or too light
if weight > 500:
    print("The object is too heavy")
elif weight < 100:
    print("The object is too light")
else:
    print("The object's weight is within acceptable range") 