'''Turtle crossing game built with pythons turtle module'''
from turtle import Screen
import time
from cars import Cars
from my_turtle import MyTurtle
from level import Level

game_in_play = True
car_speed = 1

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.bgcolor('white')
screen.tracer(0)
cars = Cars()
ted = MyTurtle()
level = Level()

screen.onkeypress(fun=ted.move_up, key='Up')
screen.onkeypress(fun=ted.move_back, key='Down')
screen.listen()



while game_in_play:
    screen.update()
    cars.move_cars(car_speed)
    time.sleep(0.1)
    for car in cars.cars:
        if ted.distance(car) < 14:
            game_in_play = False
            level.game_over()
        elif ted.ycor() > 295:
            level.level += 1
            car_speed += 0.2
            level.update_level()
            ted.move_home()

screen.exitonclick()
