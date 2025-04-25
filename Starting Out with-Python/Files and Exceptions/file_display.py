def display_numbers():
    """
    Reads and displays all numbers from numbers.txt file.
    Handles file not found errors.
    """
    try:
        # Open numbers.txt in read mode using context manager
        with open('numbers.txt', 'r') as file:
            # Iterate through each line in the file
            for number in file:
                # Remove whitespace and print each number
                print(number.strip())
    except FileNotFoundError:
        # Handle case where file doesn't exist
        print("Error: numbers.txt file not found.")

# Run only if script is executed directly
if __name__ == '__main__':
    display_numbers()