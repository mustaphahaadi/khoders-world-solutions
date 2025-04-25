def display_head():
    """
    Displays the first five lines of a user-specified file.
    If file has fewer than 5 lines, displays entire contents.
    """
    # Get filename from user
    filename = input("Enter the filename: ")
    
    try:
        # Open the specified file in read mode
        with open(filename, 'r') as file:
            # Enumerate file lines starting from 0
            for i, line in enumerate(file):
                # Display only first 5 lines (index 0-4)
                if i < 5:
                    print(line.strip())
                else:
                    break
    except FileNotFoundError:
        # Handle case where specified file doesn't exist
        print(f"Error: {filename} not found.")

if __name__ == '__main__':
    display_head()