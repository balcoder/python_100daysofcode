''' creates car with random color and positions'''
import random
from turtle import Turtle

class Car(Turtle):
    ''' Car gets color and initial position with speed '''
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(self.get_rand_color())
        self.penup()
        self.setheading(180)       
        self.goto(self.get_rand_startpos())

    def get_rand_color(self):
        colors = ["red", "green", "blue", "yellow", "violet", "purple", "brown"]
        return random.choice(colors)

    def get_rand_initpos(self):
        new_y = random.randint(-260, 260)
        return (300, new_y)

    def get_rand_startpos(self):
        new_x = random.randint(-290, 290)
        new_y = random.randint(-260, 260)
        return (new_x, new_y)


    def move(self, car_speed):
        rand_speed = random.randrange(1, 30)
        speed = rand_speed * car_speed
        self.forward(speed)
        if self.xcor() < -300:
            self.goto(self.get_rand_initpos())
