import time 
from turtle import Screen 
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white") 
screen.tracer(0)

timmy = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(timmy.go_up, "Up")
screen.onkey(timmy.go_down, "Down")

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	screen.update()

	cars.create_cars()
	cars.move_cars()

	# Detect collision with car
	for car in cars.all_cars:
		if car.distance(timmy) < 20:
			game_is_on = False

	# Detect succesful crossing
	if timmy.is_at_finish_line():
		timmy.go_to_start()
		scoreboard.score_up()


screen.exitonclick()

