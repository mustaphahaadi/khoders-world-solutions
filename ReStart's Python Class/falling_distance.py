
def falling_distance(t):
    g = 9.8
    d = 0.5 * g * t**2
    return d

# Call the function in a loop
for i in range(1, 11):
    distance = falling_distance(i)
    print(f"The distance fallen in {i} seconds is {distance} meters.")