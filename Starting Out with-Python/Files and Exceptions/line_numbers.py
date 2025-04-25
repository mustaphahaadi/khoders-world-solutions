def display_numbered_lines():
    """
    Displays file contents with line numbers.
    Each line is preceded by its number and a colon.
    """
    # Get filename from user
    filename = input("Enter the filename: ")
    
    try:
        # Open the specified file in read mode
        with open(filename, 'r') as file:
            # Enumerate lines starting from 1 instead of 0
            for line_num, line in enumerate(file, 1):
                # Format output with line number and content
                print(f"{line_num}: {line.strip()}")
    except FileNotFoundError:
        # Handle case where specified file doesn't exist
        print(f"Error: {filename} not found.")

if __name__ == '__main__':
    display_numbered_lines()