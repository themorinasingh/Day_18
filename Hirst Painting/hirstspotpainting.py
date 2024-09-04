# import colorgram
#
# colors = colorgram.extract("colors.jpg", 20)
#
# color_list = []
#
# for color in colors:
#     color_list.append(tuple(color.rgb))
#
# color_list.pop(0)
# color_list.pop(0)
# color_list.pop(0)
# color_list.pop(0)
# print(color_list)

color_list = [(56, 92, 135), (198, 162, 101), (149, 74, 53), (224, 201, 118), (134, 68, 85), (194, 185, 23), (139, 165, 190), (210, 92, 70), (64, 40, 52), (180, 19, 12), (123, 200, 160), (205, 154, 180), (30, 116, 75), (19, 171, 150), (202, 77, 81), (24, 26, 32)]
import random
import turtle as t
t.colormode(255)

tim = t.Turtle()
screen = t.Screen()
tim.shape("circle")
tim.speed(0)
def art_maker(height, width, dot_size, gap):
    for x in range(1, height):
        for y in range(0, width):
            tim.dot(dot_size, random.choice(color_list))
            tim.penup()
            tim.forward(gap)

        tim.home()
        tim.setheading(90)
        tim.forward(gap * x)
        tim.setheading(0)

art_maker(10, 10, 10, 40)
tim.hideturtle()

screen.exitonclick()