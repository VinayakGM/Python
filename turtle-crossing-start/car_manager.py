from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars=[]
        self.car_speed=MOVE_INCREMENT

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
          new_car=Turtle("square")
          new_car.shapesize(stretch_wid=1,stretch_len=1)
          new_car.penup()
          new_car.color(random.choice(COLORS))
          new_car.setheading(180)
          new_y=random.randint(-200,200)
          new_car.goto(280,new_y)
          self.all_cars.append(new_car)
    
    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def levelup(self):
        self.car_speed+=MOVE_INCREMENT
        
        
