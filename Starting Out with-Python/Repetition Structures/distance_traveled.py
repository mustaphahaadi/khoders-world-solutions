 # Get input from user
speed = float(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

# Print header
print("\nHour\tDistance Traveled")
print("-" * 25)

# Loop to calculate and display distance for each hour
for hour in range(1, hours + 1):
    distance = speed * hour
    print(f"{hour}\t{distance}")