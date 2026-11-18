from turtle import Turtle
STARTING_POSITION = (0,-250)

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_left(self):
        if self.xcor() > -370:
            self.goto(x=(self.xcor()-15),y=self.ycor())

    def move_right(self):
        if self.xcor() < 370:
            self.goto(x=(self.xcor()+15),y=self.ycor())



