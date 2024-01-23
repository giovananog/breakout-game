from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()

screen.bgcolor("black")
screen.screensize(600, 600)
screen.title("Breakout Game")
# screen.tracer(0)

player = Player((0, -290))
scoreboard = Scoreboard()
ball = Ball()

# ------------------- listeners
screen.listen()
screen.onkeypress(player.go_left, "a")
screen.onkeypress(player.go_right, "d")

# game loop
game_is_on = True
while game_is_on:
    ball.move()



# screen exit on click
screen.exitonclick()