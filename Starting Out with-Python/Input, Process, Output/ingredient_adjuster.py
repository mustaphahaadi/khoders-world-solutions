# Original recipe quantities (for 48 cookies)
SUGAR_PER_48 = 1.5
BUTTER_PER_48 = 1.0
FLOUR_PER_48 = 2.75

# Get desired number of cookies
desired_cookies = float(input("How many cookies do you want to make? "))

# Calculate ingredient amounts
sugar = (desired_cookies / 48) * SUGAR_PER_48
butter = (desired_cookies / 48) * BUTTER_PER_48
flour = (desired_cookies / 48) * FLOUR_PER_48

# Display results
print(f"\nFor {desired_cookies:.0f} cookies, you need:")
print(f"Sugar: {sugar:.2f} cups")
print(f"Butter: {butter:.2f} cups")
print(f"Flour: {flour:.2f} cups") 