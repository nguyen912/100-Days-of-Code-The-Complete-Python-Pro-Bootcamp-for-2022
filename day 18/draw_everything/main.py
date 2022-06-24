import turtle as t
import random

# turtle
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.backward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.left(180)
timmy_the_turtle.setheading(0)

# draw a square
square = t.Turtle()
square.forward(100)
square.right(90)
square.forward(100)
square.left(90)
square.backward(100)
square.right(90)
square.backward(100)

# another way to draw square
new_square = t.Turtle()
for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

# draw dashed line
dashed_line = t.Turtle()
for _ in range(10):
    dashed_line.forward(10)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()


