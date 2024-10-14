#
#
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('points.jpg', 72)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random
turtle.colormode(255)
tim = turtle.Turtle()
tim.shape("turtle")
color_list = [(231, 230, 226), (235, 226, 231), (224, 232, 227), (223, 229, 236), (39, 96, 148), (207, 161, 90), (141, 89, 57), (174, 46, 78), (224, 209, 104), (176, 164, 36), (110, 175, 208), (210, 130, 173), (207, 67, 110), (145, 27, 53), (231, 72, 47), (88, 103, 197), (21, 41, 66), (52, 166, 85), (121, 220, 210), (82, 12, 32), (31, 139, 87), (55, 29, 20), (49, 183, 194), (34, 57, 114), (118, 40, 31), (125, 194, 175), (220, 206, 29), (232, 167, 184), (29, 81, 88), (155, 208, 219), (233, 172, 164), (169, 184, 224), (10, 104, 84), (82, 69, 37)]

tim.setheading(135)
tim.penup()
tim.forward(500)
tim.setheading(0)
tim.pendown()


for i in range(8):
    for n in range(9):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(100)
        tim.pendown()
    tim.penup()
    tim.right(180)
    tim.forward(900)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.pendown()
turtle.exitonclick()
screen = tim.Screen()