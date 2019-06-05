# Import turtle module
import turtle

def draw_square(t, length):
    """
    Draw a square with a given length
    :param t: a turtle object
    :param length: an integer representing the size of a square
    :return: none
    """
    for i in range(4):
        t.fd(length)
        t.left(90)

def move_turtle(t):
    """
    Move the turtle to another position
    :param t: a turtle object
    :return: none
    """
    t.up()
    for j in range(2):
        t.right(90)
        t.fd(10)
    t.right(180)
    t.down()

# Setup a screen and a turtle
win = turtle.Screen()
win.bgcolor("lightgreen")
tito = turtle.Turtle()
tito.color("hotpink")
tito.pensize(5)

# Loop 5 times
size = 40
for i in range(5):
    # Draw a square
    draw_square(tito, size)
    size += 20
    move_turtle(tito)

# Exit the screen when click
win.exitonclick()