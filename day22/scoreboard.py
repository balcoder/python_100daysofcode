'''class to keep score of how much food the snake has eaten'''
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.computer_score = 0
        self.player_score = 0
        self.penup()
        self.color('white')
        self.goto(0, 275)
        self.hideturtle()
    
    def start_score(self):
        score =str(self.computer_score) + " : " + str(self.player_score)
        self.write(score, False, align=ALIGNMENT, font=FONT)

    def update_playerscore(self):
        self.player_score += 1
        score =str(self.computer_score) + " : " + str(self.player_score)
        self.clear()
        self.write(score, False, align=ALIGNMENT, font=FONT)
    def update_computerscore(self):
        '''uodates score'''
        self.computer_score += 1
        score =str(self.computer_score) + " : " + str(self.player_score)
        self.clear()
        self.write(score, False, align=ALIGNMENT, font=FONT)

    def update_score(self):        
        score = str(self.computer_score) + " : " + str(self.player_score)
        self.clear()
        self.write(score, False, align=ALIGNMENT, font=FONT)

    def end_game(self):
        game_over = "Game Over. Final Score: " + str(self.computer_score) + " : " + str(self.player_score)
        self.clear()
        self.goto(0, 0)
        self.write(game_over, False, align=ALIGNMENT, font=FONT)
