# Constants
DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Get input from user
people = int(input("Enter the number of people attending: "))
hot_dogs_per_person = int(input("Enter hot dogs per person: "))

# Calculate total hot dogs needed
total_hot_dogs = people * hot_dogs_per_person

# Calculate packages needed
hot_dog_packages = (total_hot_dogs + DOGS_PER_PACKAGE - 1) // DOGS_PER_PACKAGE
bun_packages = (total_hot_dogs + BUNS_PER_PACKAGE - 1) // BUNS_PER_PACKAGE

# Calculate leftovers
hot_dogs_left = (hot_dog_packages * DOGS_PER_PACKAGE) - total_hot_dogs
buns_left = (bun_packages * BUNS_PER_PACKAGE) - total_hot_dogs

# Display results
print(f"\nMinimum packages of hot dogs needed: {hot_dog_packages}")
print(f"Minimum packages of hot dog buns needed: {bun_packages}")
print(f"Hot dogs left over: {hot_dogs_left}")
print(f"Hot dog buns left over: {buns_left}") 