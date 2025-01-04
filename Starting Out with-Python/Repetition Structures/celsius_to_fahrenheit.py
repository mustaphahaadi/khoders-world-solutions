 # Print header
print("Celsius\tFahrenheit")
print("-" * 20)

# Loop through Celsius temperatures 0-20
for celsius in range(21):
    # Calculate Fahrenheit
    fahrenheit = (9/5 * celsius) + 32
    # Display the temperatures
    print(f"{celsius}\t{fahrenheit:.1f}")