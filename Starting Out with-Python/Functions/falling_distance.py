def falling_distance(time):
    """
    Calculate the distance an object falls due to gravity in a specific time period
    using the formula d = ½gt², where g is 9.8 m/s²
    """
    g = 9.8  # acceleration due to gravity in m/s²
    distance = 0.5 * g * time**2
    return distance

def main():
    print("Time (seconds)    Distance (meters)")
    print("-" * 35)
    
    # Loop through values 1-10 and display falling distances
    for time in range(1, 11):
        distance = falling_distance(time)
        print(f"{time:^15} {distance:^18.2f}")

if __name__ == "__main__":
    main()