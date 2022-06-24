import colorgram
import turtle
import random

turtle.colormode(255)
dot = turtle.Turtle()
screen = turtle.Screen()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

dot.speed("fastest")
dot.penup()
dot.hideturtle()
dot.setheading(225)
dot.forward(300)
dot.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    dot.dot(20, random.choice(rgb_colors))
    dot.forward(50)

    if dot_count % 10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)

screen.exitonclick()
