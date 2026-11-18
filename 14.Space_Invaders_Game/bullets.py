from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("Red")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.1)
        self.setheading(90)

    def fire(self,x,y):
        self.goto(x,y)
        self.showturtle()

    def move(self):
        x = self.xcor()
        y = self.ycor()+10
        self.goto(x,y)