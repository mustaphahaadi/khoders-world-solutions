def write_golf_scores():
    """
    Records golf players' names and scores to golf.txt.
    """
    try:
        with open('golf.txt', 'w') as file:
            while True:
                # Get player information
                name = input("Enter player name (or press Enter to quit): ")
                if name == '':
                    break
                    
                try:
                    score = int(input("Enter player's score: "))
                    # Write player record to file
                    file.write(f"{name},{score}\n")
                except ValueError:
                    print("Error: Please enter a valid score.")
                    
        print("Golf scores have been saved to golf.txt")
        
    except IOError:
        print("Error: Could not write to file.")

if __name__ == '__main__':
    write_golf_scores()