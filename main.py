from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
# move up
screen.listen()
screen.onkey(player.up, "Up")

# car generator
car = CarManager()
scoreboard.level_up()

# game speed controler

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    car.create_cars()
    car.move_car()


    # detect collition
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # leveling up the game
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        car.increase_speed()



screen.exitonclick()



