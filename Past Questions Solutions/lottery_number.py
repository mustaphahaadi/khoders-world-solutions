import random

# Generate a seven-digit lottery number
lottery_number = []
for i in range(7):
    lottery_number.append(random.randint(0, 9))

# Display the contents of the list
for number in lottery_number:
    print(number, end=' ') #end=' ' adds space between the numbers