'''create a ball object and methods to start moving ball'''
from turtle import Turtle

class Ball(Turtle):
    '''creates a pong ball'''
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.initialize_ball()
        self.x_move = 10
        self.y_move = 10

    def initialize_ball(self):
        self.goto(0,0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1
