###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as T
T.colormode(255)
t=T.Turtle()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    # rgb_colors.append(color.rgb)
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    tup=(r,g,b)
    rgb_colors.append(tup)

# print(rgb_colors)
t.speed("slow")
colors=[(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
i=1
import random
t.penup()
t.hideturtle()
t.setposition(-100,-100)

for i in range(1,101):
    t.dot(20,random.choice(colors))
    t.forward(50)
    if i%10 ==0 :
        t.setheading(90)
        t.forward(20)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen_obj=T.Screen()
screen_obj.exitonclick()