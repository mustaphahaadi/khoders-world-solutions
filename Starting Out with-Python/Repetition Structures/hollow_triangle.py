# Number of rows
ROWS = 6

# Loop for each row
for i in range(ROWS):
    # Print first character
    print('#', end='')
    
    # Print spaces and last character
    if i > 0:  # Skip first row since it's just ##
        # Print spaces
        for j in range(i):
            print(' ', end='')
        # Print last #
        print('#')
    else:
        # First row has two # with no space
        print('#') 