# Initialize sum
total = 0

# Explain program to user
print("Enter positive numbers to sum.")
print("Enter a negative number to end.")

# Loop until user enters a negative number
while True:
    number = float(input("\nEnter a number: "))
    
    # Check if negative
    if number < 0:
        break
        
    # Add positive number to total
    total += number

# Display the sum
print(f"\nThe sum of all positive numbers entered is: {total}") 