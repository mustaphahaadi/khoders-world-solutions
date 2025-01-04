# First step
print("Reboot the computer and try to connect.")
answer = input("Did that fix the problem? ").lower()

# Check first solution
if answer != "yes":
    # Second step
    print("Reboot the router and try to connect.")
    answer = input("Did that fix the problem? ").lower()
    
    # Check second solution
    if answer != "yes":
        # Third step
        print("Make sure the cables between the router and modem are plugged in firmly.")
        answer = input("Did that fix the problem? ").lower()
        
        # Check third solution
        if answer != "yes":
            # Fourth step
            print("Move the router to a new location.")
            answer = input("Did that fix the problem? ").lower()
            
            # Check fourth solution
            if answer != "yes":
                # Final step
                print("Get a new router.") 