'''Sets up sakes and and gives move method '''
from turtle import Turtle

STARTING_POSITIONS =  [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    ''' Creates turtles and a move method '''
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        ''' creates snakes base on number of positions '''
        for position in STARTING_POSITIONS:
            self.add_to_turtle(position)

    def add_to_turtle(self, position):
        ''' Add segment to snake '''
        new_turtle = Turtle(shape="square")
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.setposition(position)
        self.turtles.append(new_turtle)

    def extend(self):
        ''' Extend snake by one segment '''
        self.add_to_turtle(self.turtles[-1].position())

    def move(self):
        ''' moves the snakes behind head based on head movement '''
        for seq_num in range(len(self.turtles) -1, 0, -1):
            new_x = self.turtles[seq_num - 1].xcor()
            new_y = self.turtles[seq_num - 1].ycor()
            self.turtles[seq_num].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        ''' Move snake up if not moving down '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        ''' Move sanke down if not moving up '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        ''' Move snake right if not moving left '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        ''' Move sanke left if not moving right '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
