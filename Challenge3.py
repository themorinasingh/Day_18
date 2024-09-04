from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")

#drawing a triangle
for i in range(3):
    tim.forward(100)
    tim.left(120)

#drawing a square
tim.pencolor("green")
for i in range(4):
    tim.forward(100)
    tim.left(90)

#drawing a pentagon
tim.pencolor("blue")
for i in range(5):
    tim.forward(100)
    tim.left(72)

#drawing a hexagon
tim.pencolor("yellow")
for i in range(6):
    tim.forward(100)
    tim.left(60)

#drawing the septagon
tim.pencolor("red")
for i in range(7):
    tim.forward(100)
    tim.left(51.53)

#drawing the octagon
tim.pencolor("brown")
for i in range(8):
    tim.forward(100)
    tim.left(45)

screen.exitonclick()
