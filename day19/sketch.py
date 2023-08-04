from turtle import Turtle, Screen

ted = Turtle()
screen = Screen()

def move_forward():
    ted.forward(30)

def move_back():
    ted.backward(30)

def right():
    new_heading = ted.heading() - 10
    ted.setheading(new_heading)

def left():
    new_heading = ted.heading() + 10
    ted.setheading(new_heading)

def clear():
    ted.clear()
    ted.penup()
    ted.home()
    ted.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
