# import pandas

# data=pandas.read_csv("sample.csv")
# case_name=input("Enter Case Name: ")
# # data_frame=pandas.Dataframe(data)
# data_dict=data[case_name]
# print(data_dict)

import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y,guess_answer):
#     print(guess_answer)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    cnt=0
    guess_answer=screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="Whats the statename")
    guess_answer=guess_answer.capitalize()

    if guess_answer=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        newdata=pandas.DataFrame(missing_states)
        newdata.to_csv("state_to_learn.csv")
        break
    if guess_answer in all_states:
        guessed_states.append(guess_answer)
        cnt=cnt+1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==guess_answer]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(guess_answer)













# turtle.mainloop()



screen.exitonclick()
