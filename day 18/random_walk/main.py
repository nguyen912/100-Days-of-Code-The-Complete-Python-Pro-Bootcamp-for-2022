import random
import turtle

walk = turtle.Turtle()
walk.pensize(10)
# E, N, W, S
directions = (0, 90, 180, 270)


def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.colormode(255)
    return screen


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


if __name__ == '__main__':
    screen = setup_screen()
    for i in range(200):
        walk.color(random_color())
        walk.forward(30)
        walk.setheading(random.choice(directions))

    screen.exitonclick()
