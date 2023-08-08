import random
from turtle import Turtle

class Food(Turtle):
    ''' Render itself as small blue circle on screen and when gets eaten
    by snake reder itself at a new random location'''
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.move()

    def move(self):
        '''moves the food/turtle to new random position'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        