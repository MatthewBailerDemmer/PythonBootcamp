import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

points = 0
data = pandas.read_csv("50_states.csv")

game_on = True
while game_on:
    answere_state = screen.textinput(title=f"So far: {points}/50", prompt="Can you tell all the 50 american states?")
    answere_state = answere_state.title()
    if answere_state == "Exit":
        break
    found = data[data["state"] == answere_state]
    if not found.empty:
        state_index = found.index[0]
        found = found.to_dict("records")
        x_cor = int(found[0]['x'])
        y_cor = int(found[0]['y'])
        name = found[0]['state']
        writer.goto(x_cor, y_cor)
        writer.write(name)
        data = data.drop(state_index)
        points += 1
        if points == 50:
            game_on = False

if not game_on:
    writer.goto(0,0)
    writer.write("You Win!")
else:
    data.to_csv("states_to_learn.csv")


turtle.mainloop()