'''Creates a Damien Hirst dot painting using turtle'''
import random
import turtle as t
import colorgram
# import hirst-spots.jp as image

screen = t.Screen()
screen.colormode(255)
screen.setup(500, 600)


ted = t.Turtle()
ted.shape('arrow')
ted.speed(0)
ted.penup()
ted.goto(-225, -270)
ted.pendown()
ted.hideturtle()

background_color = (253, 251, 247)

colors = colorgram.extract('day18/hirst-spots.jpg', 20)

# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))

color_list = [
(232, 251, 242), (198, 13, 32), (250, 237, 19),(39, 76, 189),
(39, 217, 68), (238, 227, 5), (229, 159, 47),(28, 40, 156),
(214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11),
(243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8),
(223, 141, 209), (11, 97, 62)
]

def random_color():
    ''' returns random tuple containing rgb colors'''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def draw_hirst_spots(space = 50):
    '''Draw the spots on canvas using color list'''     
    for _ in range(10):
        for _ in range(10):
            ted.dot(30,random.choice(color_list))
            ted.penup()
            ted.forward(space)
        ted.left(90)
        ted.forward(60)
        ted.left(90)
        ted.forward(500)
        ted.right(180)

draw_hirst_spots()
print(ted.pos())
print(screen.screensize())

screen.bgcolor(background_color)
screen.exitonclick()
