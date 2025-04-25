def generate_webpage():
    """
    Creates a simple HTML webpage from user input.
    """
    try:
        # Get user input
        name = input("Enter your name: ")
        description = input("Describe yourself: ")
        
        # Create HTML content
        html_content = f"""<html>
<head>
</head>
<body>
    <center>
        <h1>{name}</h1>
    </center>
    <hr />
    {description}
    <hr />
</body>
</html>"""
        
        # Write HTML to file
        with open('personal_page.html', 'w') as file:
            file.write(html_content)
            
        print("Webpage has been created as personal_page.html")
        
    except IOError:
        print("Error: Could not create webpage file.")

if __name__ == '__main__':
    generate_webpage()