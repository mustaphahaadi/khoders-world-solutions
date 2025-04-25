import random

def write_random_numbers():
    """
    Writes user-specified number of random integers (1-500) to a file.
    """
    try:
        # Get count of numbers from user
        count = int(input("How many random numbers should be written? "))
        
        # Validate input
        if count <= 0:
            print("Please enter a positive number.")
            return
            
        # Open file in write mode
        with open('random_numbers.txt', 'w') as file:
            # Generate and write random numbers
            for _ in range(count):
                number = random.randint(1, 500)
                file.write(f"{number}\n")
                
        print(f"{count} random numbers have been written to random_numbers.txt")
        
    except ValueError:
        print("Error: Please enter a valid number.")
    except IOError:
        print("Error: Could not write to file.")

if __name__ == '__main__':
    write_random_numbers()