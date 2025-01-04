# Get input from user
while True:
    number = int(input("Enter a nonnegative integer to calculate its factorial: "))
    if number >= 0:
        break
    print("Please enter a nonnegative number.")

# Initialize factorial
factorial = 1

# Calculate factorial
if number > 0:
    print(f"\nCalculating {number}! :", end=" ")
    for i in range(1, number + 1):
        factorial *= i
        # Print multiplication steps
        if i < number:
            print(f"{i} × ", end="")
        else:
            print(f"{i} = ", end="")
else:
    print("\n0! = ", end="")

# Display result
print(factorial) 