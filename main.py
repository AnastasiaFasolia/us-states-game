import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Set the image in the background
image = "blank_states_img.gif"
turtle.bgpic(image)

# Read csv file and get x and y values
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Ask user for answer
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = [s for s in all_states if s not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        # Pull state coordinates
        state_data = data[data.state == answer_state]
        # Write state on map
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(state_data.x), int(state_data.y)) 
        turtle.write(f"{state_data.state.item()}", font=('Courier', 10, 'normal'))
       
# Keep screen open
screen.exitonclick()