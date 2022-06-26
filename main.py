from turtle import Turtle,Screen
import pandas
import turtle


game_on = True
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title('GUESS THE STATES')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
text = Turtle()

missed_answer = []
correct_guess = []
location_test = Turtle()

data = pandas.read_csv('50_states.csv')
state_list = data['state'].tolist()

while game_on:
    guess_answer = screen.textinput(prompt='What do you think next?', title=f'{len(correct_guess)}/{len(state_list)} States Correct')
    guess_answer = guess_answer.capitalize()
    state_row = data[data.state == guess_answer]

    for i in state_list:
        if i == guess_answer:
            x = int(state_row.x)
            y = int(state_row.y)
            text.goto(x, y)
            text.write(i)
            correct_guess.append(guess_answer)
            score = len(correct_guess)

    if guess_answer == 'Exit':
        for i in state_list:
            if i not in correct_guess:
                missed_answer.append(i)
                missed_data = pandas.DataFrame(missed_answer)
                missed_data.to_csv('states_to _learn')
                game_on = False
        break






