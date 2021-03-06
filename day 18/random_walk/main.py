import random
import turtle

turtle.colormode(255)

walk = turtle.Turtle()
walk.pensize(5)
# E, N, W, S
directions = (0, 90, 180, 270)


def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
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
        walk.speed(random.randrange(0, 20, 1)*1/2)
        walk.forward(30)
        walk.setheading(random.choice(directions))

    screen.exitonclick()
