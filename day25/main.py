''' Guess all 50 States '''
import turtle
import pandas as pd
from guess import Guess

guess = Guess()

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
IMAGE = "day25/blank_states_img.gif"
screen.bgpic(IMAGE)

game_is_on = True
title = "Guess the State"

while game_is_on:
    answer_state = screen.textinput(
        title, prompt="What is another States name? ")
    answer_state = answer_state.title()

    # exit game on entering secret code (Exit)
    if answer_state == "Exit":
        states_to_learn = []
        for state in guess.data.state:
            if state not in guess.correct_guess:
                states_to_learn.append(state)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("day25/states_to_learn.csv")
        break

    if answer_state in guess.correct_guess:
        title = "Already tried that State"
    else:
        guess.check_guess(answer_state)
        if guess.correct:
            title = str(guess.score) + "/50 correct"
            new_turtle = turtle.Turtle()
            turtle.penup()
            turtle.hideturtle()
            x, y = guess.get_coords(answer_state)
            turtle.goto(x, y)
            turtle.write(answer_state)
            guess.correct = False
        else:
            title = "Not a state, try again"

    if len(guess.correct_guess) >= 50:
        game_is_on = False
        new_turtle = turtle.Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.write("You got them all right.",  align='left',
                     font=('Arial', 8, 'normal'))

screen.exitonclick()
