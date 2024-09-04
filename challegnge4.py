import random
import turtle

turtle.colormode(255)

tim = turtle.Turtle()
screen = turtle.Screen()

tim.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r,g,b)

angle_list = [0, 90, 180, 270 ]

tim.pensize(5)

for i in range(random.randint(250,300)):
    tim.pencolor(random_color())

    tim.setheading(random.choice(angle_list))
    tim.forward(20)

screen.exitonclick()

