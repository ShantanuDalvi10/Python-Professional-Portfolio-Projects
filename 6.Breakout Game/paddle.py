from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.penup()
        self.goto((0,-250))

    def go_right(self):
        new_x = self.xcor() + 40

        if new_x < 380:
            self.goto(new_x,self.ycor())

    def go_left(self):
        new_x = self.xcor() - 40

        if new_x > -380:
            self.goto(new_x,self.ycor())