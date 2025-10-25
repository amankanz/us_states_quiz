import turtle
from turtle import Screen
import pandas
from write_state import SetState

screen = Screen()
screen.title("U.S States Quiz")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data =pandas.read_csv("50_states.csv")
us_states = data["state"]
# us_states = data.state.to_list()
list_states = us_states.to_list()
# print(us_states)
# list_states = us_states
set_state = SetState()
score = 0
correct_states = []

game_is_on = True
while game_is_on:
    where_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    print(where_state.title())

    if where_state.title() in list_states:
            set_state.write_state(data, us_states, where_state, list_states)
            score += 1

            if len(correct_states) < 50:
                game_is_on = False
            else:
                correct_states.append(where_state.title())
                print("correct_sates length:", len(correct_states))



turtle.mainloop()