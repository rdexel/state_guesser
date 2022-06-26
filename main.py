import csv
import turtle
import pandas as pd
from name_writer import WriteName
import csv

screen = turtle.Screen()

screen.title('United States Game')
# screen.setup(width=700, height=500)
bg_image = 'blank_states_img.gif'
screen.addshape(bg_image)

turtle.shape(bg_image)

states = pd.read_csv('50_states.csv')
state_names = states.state.tolist()

score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f'{score}/50 Correct States', prompt="What's another states name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in state_names if state not in correct_guesses]
        pd.DataFrame(missing_states).to_csv('missing_states.csv')
        break
    if answer_state in state_names and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        score += 1
        state_data = states[states.state == answer_state]
        coordinates = (int(state_data.x), int(state_data.y))
        name_writer = WriteName(coordinates, answer_state)

turtle.mainloop()
