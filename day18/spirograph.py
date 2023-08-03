''' Uses random color to draw a spirograph'''
import random
import turtle as t

screen = t.Screen()
screen.colormode(255)

def random_color():
    ''' returns random tuple containing rgb colors'''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

ted = t.Turtle()
ted.shape('turtle')
ted.speed(0)

def draw_spirograph(size_of_gap):
    '''Draw a spirograph with gaps size'''
    for _ in range(int(360 / size_of_gap)):
        ted.color(random_color())
        ted.circle(100)
        ted.setheading(ted.heading() + size_of_gap)


draw_spirograph(5)
screen.exitonclick()
