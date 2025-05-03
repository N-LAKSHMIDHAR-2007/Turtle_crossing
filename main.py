#Algorithm
# 1. Move turtle with key press, 2. create and move the cars, 3. Detect collision with the car, 4.Detect when the turtle reaches the other side
# Create the score board

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

score.scores()

screen.listen()
screen.onkey(key = "Up", fun = player.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car() #for every 6 times the while loop runs a new car will be generated
    car.move()


    #detect collision with the car
    for cars in car.all_cars: #loops thru each of the car
        if cars.distance(player) < 20: #it works on all sides
            game_is_on = False
            score.game_over()

    # Successful crossing
    if player.ycor() > 285:
        player.go_to_start()
        car.level_up()

    # score
        score.increase_score()
        score.scores()













screen.exitonclick()