def calculate_average():
    """
    Calculates and displays the average of numbers stored in numbers.txt file.
    
    Steps:
    1. Opens and reads numbers.txt
    2. Converts each line to integer
    3. Calculates average if file is not empty
    4. Handles potential errors (file not found, invalid numbers)
    5. Formats output to 2 decimal places
    """
    try:
        # Open the file in read mode using context manager
        with open('numbers.txt', 'r') as file:
            # Convert file contents to list of integers
            numbers = [int(num) for num in file]
            
            # Verify file is not empty before calculating
            if numbers:
                # Calculate average using sum/count
                average = sum(numbers) / len(numbers)
                # Format and display result with 2 decimal places
                print(f"Average of numbers: {average:.2f}")
            else:
                print("File is empty.")
                
    except FileNotFoundError:
        # Handle missing file error
        print("Error: numbers.txt file not found.")
    except ValueError:
        # Handle non-numeric data error
        print("Error: File contains invalid numbers.")

# Execute only if run as script
if __name__ == '__main__':
    calculate_average()