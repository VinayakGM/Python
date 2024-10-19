import turtle as T

t=T.Turtle()
sc=T.Screen()

# def move_fwd():
#     t.forward(10)

# challenge
# def move_fwd():
#     t.forward(10)

# def move_bwd():
#     t.backward(10)

# def counter_clockwise():
#     # t.left(45)
#     # t.forward(30)
#     t.heading()+10


# def clockwise():
#     # t.right(45)
#     # t.forward(40)
#     t.heading()+10
    

# def clear():
#     t.clear()

# sc.listen()
# sc.onkey(key="w",fun=move_fwd)
# sc.onkey(key="s",fun=move_bwd)
# sc.onkey(key="a",fun=counter_clockwise)
# sc.onkey(key="d",fun=clockwise)
# sc.onkey(key="c",fun=clear)

sc.setup(500,480)
is_raceon=False
user_bet=sc.textinput(title="Make your bet",prompt="Which turtle will win the race ? Enter the color ")
# print(user_bet)
colors=["red","blue","skyblue","yellow","green","black"]
import random
y_position=[-70,-40,-10,20,50,80]
all_turtle=[]
for i in range(0,6):
    new_turtle=T.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-200,y=y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_raceon=True

while is_raceon:
    for turtle in all_turtle:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_raceon = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



sc.exitonclick()