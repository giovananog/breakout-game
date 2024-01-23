from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from ball import Ball
from wall import Wall
import time

# screen configs
screen = Screen()
screen.bgcolor("black")
screen.screensize(600, 600)
screen.title("Breakout Game")
screen.tracer(0)

# creating the objects
player = Player((0, -290))
scoreboard = Scoreboard()
ball = Ball()
wall = Wall()


# ------------------- listeners
screen.listen()
screen.onkeypress(player.go_left, "a")
screen.onkeypress(player.go_right, "d")

# game loop
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()


    # detect collision with the top wall
    if ball.ycor() > 350:
        ball.bounce_y()
    
    # detect collision with the bottom wall
    if ball.ycor() < -350:
        scoreboard.score += 1
        scoreboard.update_scoreboard
        ball.reset_position()


    # detect collision with the side walls
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()

    # detect collision with the wall
    for i in wall.list:
        if ball.distance(i) < 30:                  
            print("Colisão com parede!")
            i.hideturtle()
            ball.bounce_y()
            i.clear()
            wall.list.remove(i)


    #Detect collision with player
    if ball.distance(player) < 40:
        ball.bounce_y()    


# screen exit on click
screen.exitonclick()