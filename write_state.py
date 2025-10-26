from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 8, 'bold')

class SetState(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self,data, us_states, where_state, list_states):
        state = data[us_states == where_state.title()]
        # state_index = list_states.index(where_state.title())
        print(state)
        # x_cord = state.x.iat[0]
        # y_cord = state.y.iat[0]
        x_cord = state.x.item()
        y_cord = state.y.item()

        # self.clear()
        self.goto(x=x_cord, y=y_cord)
        self.write(f"{where_state.title()}", align=ALIGNMENT, font=FONT)
        # self.write(f"{state.state.item()}", align=ALIGNMENT, font=FONT)