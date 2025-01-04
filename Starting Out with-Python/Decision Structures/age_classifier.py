# Get age from user
age = float(input("Enter the person's age: "))

# Classify the age and display result
if age <= 1:
    print("This person is an infant")
elif age < 13:
    print("This person is a child")
elif age < 20:
    print("This person is a teenager")
else:
    print("This person is an adult") 