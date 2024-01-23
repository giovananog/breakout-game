from turtle import Screen
from player import Player
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.screensize(600, 600)
screen.title("Breakout Game")
# screen.tracer(0)

player = Player((0, -290))
scoreboard = Scoreboard()

# ------------------- listeners
screen.listen()
screen.onkeypress(player.go_left, "a")
screen.onkeypress(player.go_right, "d")




# screen exit on click
screen.exitonclick()