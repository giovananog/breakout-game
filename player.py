from turtle import Turtle

class Player(Turtle):

    def __init__(self, x, y):
        self.player = Turtle("square")
        self.player.color("white")
        self.player.turtlesize(1, 5)
        self.player.penup()
        self.player.goto(x, y)
    
    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
    
    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())