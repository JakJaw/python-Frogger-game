import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
carmanager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left_turn, "Left")
screen.onkey(player.right_turn, "Right")

scoreboard.draw_level()

game_is_on = True
lo = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.generate()
    carmanager.move_cars()

    if player.ycor() > 280:
        scoreboard.increase_level()
        carmanager.new_map()
        player.new_map()
        scoreboard.draw_level()

    for car in carmanager.all_cars:
        if car.distance(player) < 18:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()