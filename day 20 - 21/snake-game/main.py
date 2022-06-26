import turtle
import time

def setup_screen():
    screen = turtle.Screen()
    screen.title('My segment Game')
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.tracer(0)
    return screen


if __name__ == '__main__':
    screen = setup_screen()
    segments = []
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_positions:
        segment = turtle.Turtle(shape='square')
        segment.penup()
        segment.color('white')
        segment.goto(position)
        segments.append(segment)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        for seg in segments:
            seg.forward(20)








    screen.exitonclick()
