from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle(image)
state_typer = Turtle()
state_typer.penup()
state_typer.hideturtle()
is_game_on = True

states = pandas.read_csv("50_states.csv")
state_list = states["state"].to_list()
score = 0
correct_guesses = []


while is_game_on:
    user_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="Type a state name").title()

    if user_state == "Exit":
        break

    if user_state in state_list:
        if user_state not in correct_guesses:
            correct_guesses.append(user_state)
            data = states[states.state == user_state]
            x = int(data.x)
            y = int(data.y)
            state_typer.goto(x, y)
            state_typer.write(f"{user_state}", align="center", font=("Arial", 8, "normal"))
            score += 1

    if score == 50:
        is_game_on = False
        print("Nice you Guessed all the states")

states_not_guessed = [state for state in state_list if state not in correct_guesses]

state_dict = {
    "states missed": states_not_guessed
}

state_data = pandas.DataFrame(state_dict)
state_data.to_csv("state_data.csv")
