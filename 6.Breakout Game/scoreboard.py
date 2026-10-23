from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}   Lives:{self.lives}",
            align="center",
            font=("Arial",16,"normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(
            "GAME OVER",
            align="center",
            font=("Arial",28,"bold")
        )

    def win(self):
        self.goto(0,0)
        self.color("green")
        self.write(
            "You Win",
            align="center",
            font=("Arial",28,"bold")
        )