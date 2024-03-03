import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
gussed_state = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(gussed_state)<50:


    answer_state = screen.textinput(title=f"{len(gussed_state)}/50 States correct",prompt="what's another state name?").title()
    if answer_state == "Exit":
        break
    if (answer_state in all_states):
        t = turtle.Turtle()
        gussed_state.append(answer_state)
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
    # print("yes")

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)    
# turtle.mainloop()

left_states = {"state_name":[]}
for state in all_states:
    if state not in gussed_state:
        left_states["state_name"].append(state)

df = pandas.DataFrame(left_states)
df.to_csv("missed_states.csv")        