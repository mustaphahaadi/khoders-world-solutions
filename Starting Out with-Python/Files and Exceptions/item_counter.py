def count_names():
    """
    Counts and displays the number of names stored in names.txt.
    Each line is assumed to contain one name.
    """
    try:
        # Open names.txt in read mode
        with open('names.txt', 'r') as file:
            # Read all lines and count them using len()
            count = len(file.readlines())
            # Display the total count of names
            print(f"Number of names in the file: {count}")
    except FileNotFoundError:
        # Handle case where file doesn't exist
        print("Error: names.txt file not found.")

if __name__ == '__main__':
    count_names()