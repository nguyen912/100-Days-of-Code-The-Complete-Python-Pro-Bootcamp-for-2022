import turtle
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size):
    circle = turtle.Turtle()
    for i in range(int(360 / size)):
        circle.color(random_color())
        circle.speed(random.randrange(0, 20, 1) * 1 / 2)
        circle.circle(100)
        circle.setheading(circle.heading() + size)


if __name__ == '__main__':
    draw_spirograph(36)
    screen = turtle.Screen()
    screen.exitonclick()
