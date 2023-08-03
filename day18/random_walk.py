''' Random walk with turtle module '''
import random
import turtle as t

screen = t.Screen()
screen.colormode(255)


ted = t.Turtle()
ted.shape('turtle')

def random_color():
    ''' returns random tuple containing rgb colors'''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def random_walk(steps):
    '''create random walk with random colors'''
    angles = [0, 45, 90, 180]
    ted.pensize(14)
    ted.speed(0)
    for _ in range(steps):
        angle = random.choice(angles)       
        turn = random.choice(["right","left"])
        ted.color(random_color())
        if turn == "right":
            ted.right(angle)
        else:
            ted.left(angle)
        ted.forward(30)

random_walk(80)


screen.exitonclick()
