def calculate_monthly_averages():
    """
    Calculates average steps per month from steps.txt file.
    """
    # Days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    try:
        with open('steps.txt', 'r') as file:
            # Read all steps into a list
            steps = [int(line.strip()) for line in file]
            
            # Calculate monthly averages
            start_day = 0
            for month, days in enumerate(days_in_month):
                # Get steps for current month
                month_steps = steps[start_day:start_day + days]
                # Calculate and display average
                monthly_average = sum(month_steps) / days
                print(f"{months[month]}: {monthly_average:.1f} steps")
                start_day += days
                
    except FileNotFoundError:
        print("Error: steps.txt file not found.")
    except ValueError:
        print("Error: File contains invalid step counts.")
    except IOError:
        print("Error: Could not read the file.")

if __name__ == '__main__':
    calculate_monthly_averages()