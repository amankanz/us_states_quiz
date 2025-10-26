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
    where_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    print(where_state)

    if where_state == "Exit":
       break

    state_dict = {
        "Missing States": [],
        "x": [],
        "y": []
    }
    # missing_states = []
    for mis_state in list_states:
        if mis_state not in correct_states:
            # missing_states.append(mis_state)
            state = data[us_states == mis_state]
            state_dict["Missing States"].append(state.state.item())
            state_dict["x"].append(state.x.item())
            state_dict["y"].append(state.y.item())

    # Create the dataframe
    states_to_learn = pandas.DataFrame(state_dict)
    states_to_learn.to_csv("states_to_learn.csv")

    if where_state in list_states:
            set_state.write_state(data, us_states, where_state, list_states)
            score += 1

            if len(correct_states) == 50:
                game_is_on = False
            else:
                correct_states.append(where_state.title())
                print("correct_sates length:", len(correct_states))

# turtle.mainloop()

# states_to_learn.csv
# Save the missing states to csv
#list_states
#correct_states
# missing_states = list_states

# for state in list_states:
#     for cor_state in correct_states:
#         if cor_state != state:
#             missing_states.append(missing_states)

# state_dict = {
#     "Missing States": [],
#     "x": [],
#     "y": []
# }

# for mis_state in missing_states:
#     for correct_state in correct_states:
#         if correct_state == mis_state:
#             missing_states.remove(mis_state)
#
#     state = data[us_states == mis_state]
#     state_dict["Missing States"].append(state.state.item())
#     state_dict["x"].append(state.x.item())
#     state_dict["y"].append(state.y.item())

# print(missing_states)
# print("Missing state are:", len(missing_states))
#
# # Create the dataframe
# states_to_learn = pandas.DataFrame(state_dict)
# states_to_learn.to_csv("states_to_learn.csv")

# print(states_to_learn)
# print(state_dict)



