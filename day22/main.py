'''main starting point for pong game'''
import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Python PONG")
screen.tracer(0) # stops the animation
scoreboard = Scoreboard()
scoreboard.update_score()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    ball.x_move += 2
    ball.y_move += 2
    
    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    # Detect collision with right paddle
    if ball.distance(right_paddle) < 40:    # or ball.xcor() > 340:
        ball.hit_paddle()

    # Detect collision with left paddle
    if ball.distance(left_paddle) < 40:  # or ball.xcor() < -340:
        ball.hit_paddle()
    
    # Detect if ball has gone out
    if ball.xcor() > 380:
        scoreboard.update_playerscore()
        ball.initialize_ball()
        time.sleep(0.5)
    elif ball.xcor() < -380:
        scoreboard.update_computerscore()
        ball.initialize_ball()
        time.sleep(0.5)   

screen.exitonclick()
