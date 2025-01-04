# Get weight and height from user
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

# Calculate BMI
bmi = (weight * 703) / (height ** 2)

# Determine weight status
if bmi < 18.5:
    status = "underweight"
elif bmi <= 25:
    status = "optimal weight"
else:
    status = "overweight"

# Display results
print(f"\nYour BMI is: {bmi:.1f}")
print(f"You are considered {status}") 