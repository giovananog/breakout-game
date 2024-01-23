from turtle import Screen
from player import Player

screen = Screen()

screen.bgcolor("black")
screen.screensize(600, 600)
# screen.tracer(0)

player = Player(0, -290)


screen.exitonclick()