# Number of rows
ROWS = 7

# Loop for each row
for i in range(ROWS, 0, -1):
    # Print stars for current row
    for j in range(i):
        print('*', end='')
    # Move to next line
    print() 