import turtle as t
import random

t.colormode(255)
# # draw different shapes
screen = t.Screen()
screen.setup(width=1.0, height=1.0)

shape = t.Turtle()
shape.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        shape.forward(100)
        shape.left(angle)


for starting_num_side in range(3, 12):
    shape.color(random_color())
    draw_shapes(starting_num_side)

screen.exitonclick()