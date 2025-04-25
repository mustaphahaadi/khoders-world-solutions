full_name = input("Enter first, middle and last names: ")

#splitted the string to a list ["Ibrahim", "Umar", "Quanda"]
split_names = full_name.split(" ") 

#an empty string to hold the initials
initials = ""

# a loop to iterate through the list and get the initials
for name in split_names:
    initials += name[0] +"."

print(initials)


