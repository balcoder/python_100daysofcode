''' Snake game made using built in python module trutle'''
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
# screen.onkey(key="c", fun=snake.clear)

game_is_on = True
scoreboard.update_scoreboard()
while game_is_on:
    screen.update()
    
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    # turtle.distance(x, y) returns the distance from the turtle to (x,y),
    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        food.move()
        snake.extend()

    # detect collision with wall
    if (snake.head.xcor() > 298 or snake.head.xcor() < -298 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset_game()
        snake.reset_snake()
        # game_is_on = False
        # scoreboard.end_game()

    # Detect collision with tail
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.reset_game()
            snake.reset_snake()
            # game_is_on = False
            # scoreboard.end_game()
screen.exitonclick()
