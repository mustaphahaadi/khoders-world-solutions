def read_random_numbers():
    """
    Reads numbers from random_numbers.txt and displays statistics.
    """
    try:
        # Open file in read mode
        with open('random_numbers.txt', 'r') as file:
            # Read and convert all numbers to integers
            numbers = [int(line.strip()) for line in file]
            
            # Display all numbers
            print("Numbers in file:")
            for num in numbers:
                print(num)
            
            # Calculate and display statistics
            print(f"\nTotal of numbers: {sum(numbers)}")
            print(f"Count of numbers: {len(numbers)}")
            
    except FileNotFoundError:
        print("Error: random_numbers.txt not found. Run the writer program first.")
    except ValueError:
        print("Error: File contains invalid numbers.")
    except IOError:
        print("Error: Could not read the file.")

if __name__ == '__main__':
    read_random_numbers()