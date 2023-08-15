''' turtle that user guides across road '''
from turtle import Turtle

TURTLE_HOME = (0, -285)
class MyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('black')
        self.penup()
        self.left(90)
        self.goto(TURTLE_HOME)
    
    def move_up(self):
        self.forward(10)
    
    def move_back(self):
        self.backward(10)
    
    def move_home(self):
        self.goto(TURTLE_HOME)
