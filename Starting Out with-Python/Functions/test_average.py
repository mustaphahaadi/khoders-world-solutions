def calc_average(score1, score2, score3, score4, score5):
    """Calculate the average of five test scores"""
    return (score1 + score2 + score3 + score4 + score5) / 5

def determine_grade(score):
    """
    Determine the letter grade based on a test score
    using the following scale:
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        # Get five test scores from the user
        print("Enter five test scores:")
        score1 = float(input("Test score 1: "))
        score2 = float(input("Test score 2: "))
        score3 = float(input("Test score 3: "))
        score4 = float(input("Test score 4: "))
        score5 = float(input("Test score 5: "))
        
        # Validate input
        scores = [score1, score2, score3, score4, score5]
        for i, score in enumerate(scores, 1):
            if score < 0 or score > 100:
                print(f"Error: Test score {i} must be between 0 and 100.")
                return
        
        # Calculate the average
        average = calc_average(score1, score2, score3, score4, score5)
        
        # Display each score and its letter grade
        print("\nResults:")
        print("-" * 30)
        print("Score\tLetter Grade")
        print("-" * 30)
        
        for i, score in enumerate(scores, 1):
            grade = determine_grade(score)
            print(f"Test {i}: {score:.1f}\t{grade}")
        
        # Display the average and its letter grade
        average_grade = determine_grade(average)
        print("-" * 30)
        print(f"Average: {average:.1f}\t{average_grade}")
        
    except ValueError:
        print("Error: Please enter valid numbers for all test scores.")

if __name__ == "__main__":
    main()