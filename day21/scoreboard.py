'''class to keep score of how much food the snake has eaten'''
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, -290)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        score = "Score: " + str(self.score)
        self.clear()
        self.write(score, False, align=ALIGNMENT, font=FONT)

    def end_game(self):
        game_over = "Game Over. Final Score: " + str(self.score)
        self.clear()
        self.goto(0, 0)
        self.write(game_over, False, align=ALIGNMENT, font=FONT)
