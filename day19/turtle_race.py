''' Turtle racing using turtle module from python'''
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which trutle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for index, color in enumerate(colors):
    turtle_name = "ted" + str(index)
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(color)
    turtle_name.penup()
    y_coord = 100 - index * 40
    turtle_name.goto(-240, y_coord)
    all_turtles.append(turtle_name)
    

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            if user_bet == turtle.color()[0]:
                print(f"You win. {turtle.color()[0]} won the race")
                break                
            else:
                print(f"You lost. {turtle.color()[0]} won the race")
                break         
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
