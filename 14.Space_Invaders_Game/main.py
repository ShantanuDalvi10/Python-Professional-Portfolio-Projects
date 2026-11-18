from turtle import Screen, TNavigator, TPen
from spaceship import Spaceship
from bullets import Bullet
from aliens import AlienManager


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Space Invaders")
screen.tracer(0)

ship = Spaceship()
alien = AlienManager()

bullets = []

def shoot():
    bullet = Bullet()
    x = ship.xcor()
    y = ship.ycor()+15
    bullet.fire(x=x,y=y)
    bullets.append(bullet)





def move_bullet():
    for bullet in bullets[:]:
        bullet.move()
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullets.remove(bullet)
    alien.check_collision(bullets)
    screen.update()
    screen.ontimer(move_bullet,100)

screen.listen()
screen.onkey(ship.move_left,"Left")
screen.onkey(ship.move_right,"Right")
screen.onkey(shoot,"space")

def create_alien():
    alien.create_alien()
    screen.update()
    screen.ontimer(create_alien,300)

def move_aliens():
    alien.move_aliens()
    screen.update()
    screen.ontimer(move_aliens,300)


create_alien()
move_aliens()
move_bullet()


screen.exitonclick()
