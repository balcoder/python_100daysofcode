'''Turtle Art Creater'''
from turtle import Turtle, Screen
import random

ted = Turtle()
ted.shape('turtle')
ted.color("deep sky blue")

colors = [
    "blue", "dark goldenrod", "yellow", "blue violet", "magenta",
     "orange red", "green yellow", "blue"
     ]
def draw_shape(num_sides, size):
    '''draws a shape given number of sides and size'''
    angle = 360/num_sides
    for _ in range(num_sides):
        ted.forward(size)
        ted.right(angle)

for num_sides_shape in range(3, 11):
    ted.color(random.choice(colors))
    draw_shape(num_sides_shape, 100)



screen = Screen()
screen.exitonclick()
