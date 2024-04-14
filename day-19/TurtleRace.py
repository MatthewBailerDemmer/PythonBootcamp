from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
turtles = []
colors = ["red", "orange", "yellow", "green","blue", "purple"]
user_bet = str(screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:"
                                                              " \n (red, orange, yellow, green, blue or purple)")).lower()
condition = user_bet in colors

while not condition:
    user_bet = str(screen.textinput(title="Make your bet", prompt="Choose an apropriate color:"
                                                                  " \n (red, orange, yellow, green, blue or purple)")).lower()
    condition = user_bet in colors


def start_position(tim, index, color):
    tim.penup()
    tim.color(color)
    tim.goto(x=-230, y=(-100) + index * 30)
    turtles.append(tim)


for i in range(6):
    new_turtle = Turtle("turtle")
    start_position(new_turtle, i, colors[i])

if user_bet:
    is_race_on = True
print(turtles)
while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")
            break


screen.exitonclick()