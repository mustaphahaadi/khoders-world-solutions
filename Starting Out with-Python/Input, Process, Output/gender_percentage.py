# Get number of males and females
males = int(input("Enter the number of males: "))
females = int(input("Enter the number of females: "))

# Calculate total and percentages
total = males + females
male_percentage = (males / total) * 100
female_percentage = (females / total) * 100

# Display results
print(f"\nPercentage of males: {male_percentage:.1f}%")
print(f"Percentage of females: {female_percentage:.1f}%") 