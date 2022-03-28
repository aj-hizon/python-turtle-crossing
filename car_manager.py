from turtle import Turtle
import random

COLORS = ["red","orange","yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
rand_color = random.choice(COLORS)
rand_x = random.randrange(260, 300)
rand_y = random.randrange(-260, 300)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2,5)
        self.color(rand_color)
        self.goto(rand_x, rand_y)
    
    def move_cars(self):
        pass
    
   
