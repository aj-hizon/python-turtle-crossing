import time 
from turtle import Screen 
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

timmy = Player()
cars = CarManager()

screen.listen()
screen.onkey(fun= timmy.go_up, key="Up")
screen.onkey(fun= timmy.go_down, key="Down")


game_is_on = True 
while game_is_on:
	
	time.sleep(0.1)
	screen.update()
	

