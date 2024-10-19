import turtle as T


# turtle_obj=Turtle()
# turtle_obj.shape("circle")
# turtle_obj.color("black")
# turtle_obj.forward(100)
# turtle_obj.left(90)
# turtle_obj.forward(100)
# turtle_obj.left(90)
# turtle_obj.forward(100)
# # turtle_obj.forward(100)
# turtle_obj.left(90)
# turtle_obj.forward(100)

# challenge 2
t=T.Turtle()
T.colormode(255)

# for _ in range(15):
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.forward(10)


# challenge3
# num_sides=3
# def draw_shape(num_sides):
#    angle=360/num_sides
#    for _ in range(num_sides):
#       t.forward(100)
#       t.right(angle)

# for _ in range(4):
#    draw_shape(num_sides)
#    num_sides+=1
#    t.color("red")
   
    
# challenge - 4
import random
t.speed("fastest")
def random_colrs():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

# colors=["red","blue","green","yellow"]
# directions=[0,90,180,270]
# t.pensize(7)

# t.speed("slow")
# for _ in range(500):
#     rgb=random_colrs()
#     t.color(rgb)
#     t.forward(20)
#     t.setheading(random.choice(directions))
 
def spirograph(size_of_gap):
   for _ in range(int(360/size_of_gap)):
      t.color(random_colrs())
      t.circle(100)
      t.setheading(t.heading()+10)

spirograph(5)

screen_obj=T.Screen()
screen_obj.exitonclick()