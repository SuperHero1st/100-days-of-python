import turtle
import pandas
from write_class import Writer

states_data = pandas.read_csv("50_states.csv")
print(type(states_data))
writer = Writer()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answers= []

while len(correct_answers)<50 :
    answer = screen.textinput(title = f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?").title()
    if answer =="Exit":
        break
    state_row = states_data[states_data.state ==answer]
    if not state_row.empty and answer not in correct_answers:
        state_position = (state_row.x.item(), state_row.y.item())   ## The state.row.x returns the data with the index, e.g: (34 175), we use .item() to extract only the data without the index: 175
        writer.write_text(state_position, answer)
        correct_answers.append(answer)

all_states = states_data.state.to_list()
for answer in correct_answers:
    if answer in all_states:
        all_states.pop(all_states.index(answer))
missed_states = {
    "missed_states": all_states
}

missed_data = pandas.DataFrame(missed_states)
missed_data.to_csv("missed_states.csv")