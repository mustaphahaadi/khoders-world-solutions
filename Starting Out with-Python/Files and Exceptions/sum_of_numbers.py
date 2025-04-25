def calculate_sum():
    """
    Calculates and displays the sum of all numbers in numbers.txt.
    Handles both file not found and invalid number format errors.
    """
    try:
        # Open numbers.txt in read mode
        with open('numbers.txt', 'r') as file:
            # Convert each line to int and calculate sum
            total = sum(int(num) for num in file)
            # Display the total
            print(f"Sum of numbers: {total}")
    except FileNotFoundError:
        # Handle case where file doesn't exist
        print("Error: numbers.txt file not found.")
    except ValueError:
        # Handle case where file contains non-numeric data
        print("Error: File contains invalid numbers.")

if __name__ == '__main__':
    calculate_sum()