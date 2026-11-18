from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

class AlienManager:
    def __init__(self):
        self.all_aliens = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_alien(self):
        random_chance = random.randint(0,6)
        if random_chance == 1:
            new_alien = Turtle("square")
            new_alien.shapesize(stretch_wid=1,stretch_len=1)
            new_alien.penup()
            new_alien.color(random.choice(COLORS))
            random_x = random.randint(-250,250)
            new_alien.goto(random_x,300)
            new_alien.setheading(90)
            self.all_aliens.append(new_alien)

    def move_aliens(self):
        for alien in self.all_aliens:
            alien.backward(self.speed)

    def check_collision(self,bullets):
        for bullet in bullets[:]:
            for alien in self.all_aliens[:]:
                if alien.distance(bullet) < 15:
                    alien.hideturtle()
                    self.all_aliens.remove(alien)
                    bullet.hideturtle()
                    bullets.remove(bullet)
