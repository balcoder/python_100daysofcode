''' Write level to screen and update '''
from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.goto(-290, 275)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        level = "Level: " + str(self.level)
        self.write(level, move=False, align='left', font=('Arial', 16, 'normal') )

    def game_over(self):
        self.goto(-90, 0)
        self.write("Splat! Game Over", move=False, align='left', font=('Arial', 20, 'bold') )
