import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
# for _ in range(10):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

for _ in range(10):
    turtle.pencolor("black")
    turtle.forward(5)
    turtle.pencolor("white")
    turtle.forward(5)


screen.exitonclick()