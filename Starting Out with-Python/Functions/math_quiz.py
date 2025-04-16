import random

def generate_addition_problem():
    """Generate two random numbers for an addition problem"""
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    return num1, num2

def check_answer(num1, num2, user_answer):
    """Check if the user's answer is correct"""
    correct_answer = num1 + num2
    return user_answer == correct_answer, correct_answer

def main():
    # Generate random numbers for addition
    num1, num2 = generate_addition_problem()
    
    # Display the problem
    print("Math Quiz - Addition")
    print(f"  {num1}")
    print(f"+ {num2}")
    print("------")
    
    try:
        # Get answer from user
        user_answer = int(input("Enter your answer: "))
        
        # Check if the answer is correct
        is_correct, correct_answer = check_answer(num1, num2, user_answer)
        
        # Display appropriate message
        if is_correct:
            print("Congratulations! That's correct.")
        else:
            print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")
    except ValueError:
        print("Error: Please enter a valid whole number.")

if __name__ == "__main__":
    main()