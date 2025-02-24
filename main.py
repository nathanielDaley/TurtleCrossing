import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

INITIAL_GAME_SPEED = 0.1
GAME_SPEED_INCREASE = 0.8
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
# Stops the screen from performing its normal rendering and animations
screen.tracer(0)

scoreboard = Scoreboard()

car_manager = CarManager()

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_speed = INITIAL_GAME_SPEED
game_running = True
while game_running:
    time.sleep(game_speed)
    screen.update()

    car_manager.move_cars()

    if car_manager.check_collision(player.position()):
        scoreboard.game_over()
        game_running = False
    elif player.ycor() >= FINISH_LINE_Y:
        scoreboard.increase_score()
        player.goto_start()
        game_speed *= GAME_SPEED_INCREASE

screen.exitonclick()