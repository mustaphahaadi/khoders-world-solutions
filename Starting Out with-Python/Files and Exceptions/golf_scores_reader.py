def read_golf_scores():
    """
    Displays golf scores from golf.txt file.
    """
    try:
        print("\nGolf Scores:")
        print("-" * 30)
        print("Player Name\tScore")
        print("-" * 30)
        
        with open('golf.txt', 'r') as file:
            for line in file:
                # Split each line into name and score
                name, score = line.strip().split(',')
                print(f"{name}\t\t{score}")
                
    except FileNotFoundError:
        print("Error: golf.txt not found. Record some scores first.")
    except IOError:
        print("Error: Could not read the file.")
    except ValueError:
        print("Error: File contains invalid data format.")

if __name__ == '__main__':
    read_golf_scores()