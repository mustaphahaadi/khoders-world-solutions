# Get dietary restrictions
vegetarian = input("Is anyone in your party a vegetarian? ").lower().startswith('y')
vegan = input("Is anyone in your party a vegan? ").lower().startswith('y')
gluten_free = input("Is anyone in your party gluten-free? ").lower().startswith('y')

# Print header for results
print("\nHere are your restaurant choices:")

# Check each restaurant against the restrictions and display if compatible
if not vegetarian and not vegan and not gluten_free:
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Café")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
    
elif not vegan and not gluten_free:
    print("Mama's Fine Italian")
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")
    
elif not vegan:
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")
    
else:
    print("Corner Café")
    print("The Chef's Kitchen") 