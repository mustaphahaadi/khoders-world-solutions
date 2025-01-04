import turtle
import math

# Set up the turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("STOP Sign")

# Constants
SIDE_LENGTH = 100
ANGLE = 45  # 360 / 8 sides = 45 degrees
RED = '#C23B22'  # Stop sign red

# Function to center the turtle
def center_turtle():
    t.penup()
    # Move slightly up to center the octagon
    t.goto(0, SIDE_LENGTH/2)
    t.pendown()

# Set up turtle properties
t.speed(0)  # Fastest speed
t.pensize(3)

# Draw the STOP sign
center_turtle()

# Fill color for octagon
t.fillcolor(RED)
t.begin_fill()

# Draw octagon
for _ in range(8):
    t.forward(SIDE_LENGTH)
    t.right(ANGLE)

t.end_fill()

# Write "STOP"
t.penup()
t.goto(0, 0)  # Center position
t.color('white')
t.write("STOP", align="center", font=("Arial", 36, "bold"))

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop() 