import turtle
import math

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90           # Angle of north direction
SOUTH = 270         # Angle of south direction
EAST = 0            # Angle of east direction
WEST = 180          # Angle of west direction

# Setup the window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target
target = turtle.Turtle()
target.hideturtle()
target.penup()
target.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
target.pendown()
target.setheading(EAST)
target.forward(TARGET_WIDTH)
target.setheading(NORTH)
target.forward(TARGET_WIDTH)
target.setheading(WEST)
target.forward(TARGET_WIDTH)
target.setheading(SOUTH)
target.forward(TARGET_WIDTH)
target.penup()

# Center the turtle
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user
angle = float(input("Enter the projectile's angle (0-90): "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance
distance = force * FORCE_FACTOR

# Calculate the projectile's destination
radian = math.radians(angle)
target_x = distance * math.cos(radian)
target_y = distance * math.sin(radian)

# Launch the projectile
turtle.pendown()
turtle.goto(target_x, target_y)

# Did it hit the target?
is_hit = (target_x >= TARGET_LLEFT_X and
         target_x <= (TARGET_LLEFT_X + TARGET_WIDTH) and
         target_y >= TARGET_LLEFT_Y and
         target_y <= (TARGET_LLEFT_Y + TARGET_WIDTH))

# Display message and hints
if is_hit:
    print('Target hit!')
else:
    print('You missed the target.')
    
    # Provide hints for angle
    if target_y < TARGET_LLEFT_Y:
        print('Try a greater angle')
    elif target_y > (TARGET_LLEFT_Y + TARGET_WIDTH):
        print('Try a smaller angle')
        
    # Provide hints for force
    if target_x < TARGET_LLEFT_X:
        print('Use more force')
    elif target_x > (TARGET_LLEFT_X + TARGET_WIDTH):
        print('Use less force')

turtle.done() 