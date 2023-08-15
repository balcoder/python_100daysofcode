'''class to keep score of how much food the snake has eaten'''
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('day21/data.txt', 'r') as file:
            high_score = int(file.read())
        self.score = high_score
        self.high_score = 0
        self.penup()
        self.color('white')
        self.goto(0, -290)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        score = "Score: " + str(self.score) +f": High Score:{self.high_score}"
        self.clear()
        self.write(score, False, align=ALIGNMENT, font=FONT)
    
    def update_scoreboard(self):
        self.clear()
        score = "Score: " + str(self.score) +f": High Score:{self.high_score}"
        self.write(score, False, align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_to_data(self.high_score)
        self.score = 0
        self.update_scoreboard()
    
    def write_to_data(self,score):
        with open('day21/data.txt', 'w') as file:
            file.write(str(score))

    # def end_game(self):
    #     game_over = "Game Over. Final Score: " + str(self.score)
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(game_over, False, align=ALIGNMENT, font=FONT)
