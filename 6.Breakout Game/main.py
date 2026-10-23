from turtle import Screen, TNavigator, TPen

from scoreboard import Scoreboard
from brick import Brick
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

bricks = []
colors = ["red","blue","orange","yellow","green"]

for row in range(5):
    for column in range(10):
        x = -330 + column * 73
        y = 230 - row * 30

        brick = Brick(x,y,colors[row])
        bricks.append(brick)

screen.listen()
screen.onkey(paddle.go_left,"Left")
screen.onkey(paddle.go_right,"Right")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Ball bounces after hitting side walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Ball bounces after hitting top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Ball bounces after hitting paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -235:
        ball.bounce_y()

    # If ball falls below paddle
    if ball.ycor() < -330:
        scoreboard.lose_life()

        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_is_on = False
        else:
            ball.reset_position()
            time.sleep(0.5)


    # Destroys brick after ball collides with it
    for brick in bricks[:]:
        if(
            ball.xcor() > brick.xcor() - 35
            and ball.xcor() < brick.xcor() + 35
            and ball.ycor() > brick.ycor() - 18
            and ball.ycor() < brick.ycor() + 18
        ):
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.increase_score()
            ball.bounce_y()
            break

    if len(bricks) == 0:
        scoreboard.win()
        game_is_on = False

screen.exitonclick()