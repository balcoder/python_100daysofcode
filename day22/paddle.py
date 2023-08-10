''' class to create and move a paddle '''
from turtle import Turtle
class Paddle(Turtle):
    ''' creates a paddle given a tuple of x/y coordinates'''
    def __init__(self, position):
        super().__init__()
        self.rect_cors = ((-50,10),(50,10),(50,-10),(-50,-10))
        self.screen.register_shape('rectangle',self.rect_cors)
        self.shape('rectangle')
        self.penup()
        self.color('white')
        self.goto(position)

    def go_up(self):
        '''move paddle up'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        '''move paddle down'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

# could also create the shape using a square and stretching
# class Paddle(Turtle):
#     ''' creates a paddle given a tuple of x/y coordinates'''
#     def __init__(self, position):
#         super().__init__()
        
#         self.shape('square')
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.color('white')        
#         self.goto(position)