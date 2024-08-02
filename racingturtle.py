import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)


user_input = screen.textinput(title="Make you bet!", prompt="Which turtle shall win? Enter a color: ")


color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]


all_turtle = []

for var in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[var])
    new_turtle.goto(x=-230, y=y_pos[var])
    all_turtle.append(new_turtle)

race_is_on = False
if user_input:
    race_is_on = True

while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print("You Won!")
            else:
                print(f"You lost. {winning_color} won.")
        turtle_distance = random.randint(0, 10)
        turtle.forward(turtle_distance)
screen.exitonclick()
