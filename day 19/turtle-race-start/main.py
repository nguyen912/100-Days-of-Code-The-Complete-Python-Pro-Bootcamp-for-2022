import random
from turtle import Turtle, Screen

if __name__ == '__main__':
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title('Bet Game')
    user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color')

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    y_position = [-70, -40, -10, 20, 50, 80]

    turtles = []
    for turtle_index in range(0, 6):
        turtle = Turtle(shape='turtle')
        turtle.color(colors[turtle_index])
        turtle.penup()
        turtle.goto(x=-230, y=y_position[turtle_index])
        turtles.append(turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()