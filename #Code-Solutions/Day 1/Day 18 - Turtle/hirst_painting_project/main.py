def cologram():
    # import colorgram

    # rgb_colors = []
    # colors = colorgram.extract('image.jpg', 30)

    # for color in colors:
    #     rgb = color.rgb

    #     red = rgb.r
    #     green = rgb.g
    #     blue = rgb.b
    #     color_tuple = (red, green, blue)
    #     rgb_colors.append(color_tuple)
    pass
color_list= [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import turtle as t
import random

super = t.Turtle()
t.colormode(255)
t.speed(0)

t.penup()
t.setposition(-200,-200)


def draw_dot_row(y_pos):
    for i in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)

    t.setposition(-200, y_pos)

offset = 50
for y_pos in range(-150, -150 +(offset*10), offset):
    draw_dot_row(y_pos)

t.hideturtle()

screen = t.Screen()
screen.exitonclick()