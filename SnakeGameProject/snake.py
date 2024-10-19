from turtle import Turtle as T

pos=[(0,0),(-20,0),(-40,0)]
MOVEDISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=360


class Snake:


    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    
    def createsnake(self):
        for i in pos:
           self.add_turtle(i)
          
      
    def add_turtle(self,i):
           new_turtle=T(shape="square")
           new_turtle.color("white")
           new_turtle.penup()
           new_turtle.goto(i)
           self.segments.append(new_turtle)
    
    def extend(self):
          self.add_turtle(self.segments[-1].position())
        
    def reset(self):
          for seg in self.segments:
              seg.goto(1000,1000)
          self.segments.clear()
          self.createsnake()
          self.head=self.segments[0]
    
    def move(self):
         for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
         self.head.forward(MOVEDISTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
          self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
          self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading()!=RIGHT:
          self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
          self.head.setheading(RIGHT)
