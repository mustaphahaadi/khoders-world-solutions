def max(num1, num2):
    """Return the greater of two integer values"""
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    try:
        # Get two integer values from the user
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        
        # Find and display the maximum value
        maximum = max(num1, num2)
        print(f"The maximum value is: {maximum}")
    except ValueError:
        print("Error: Please enter valid integer values.")

if __name__ == "__main__":
    main()