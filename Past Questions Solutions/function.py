def initials(name):
    #splitted the string to a list ["Ibrahim", "Umar", "Quanda"]
    split_names = full_name.split(" ") 

    #an empty string to hold the initials
    initials = ""

    # a loop to iterate through the list and get the initials
    for i in split_names:
        initials += i[0] +"."

    print(initials)

full_name = input("Enter first, middle and last names: ")
initials(full_name)
