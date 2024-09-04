import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
screen = t.Screen()
tim.speed(0)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

def draw_a_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_a_spirograph(1)

screen.exitonclick()