def kinetic_energy(mass, velocity):
    """
    Calculate the kinetic energy of an object
    using the formula KE = ½mv², where:
    - m is the object's mass in kilograms
    - v is the object's velocity in meters per second
    """
    return 0.5 * mass * velocity**2

def main():
    try:
        # Get mass and velocity from the user
        mass = float(input("Enter the object's mass (in kilograms): "))
        velocity = float(input("Enter the object's velocity (in meters per second): "))
        
        # Validate input
        if mass < 0:
            print("Error: Mass cannot be negative.")
            return
            
        # Calculate and display the kinetic energy
        energy = kinetic_energy(mass, velocity)
        print(f"\nThe object's kinetic energy is {energy:.2f} joules.")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()