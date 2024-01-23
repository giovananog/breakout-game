from turtle import Turtle

class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.penup()
        self.goto(position)
    
    def go_right(self):
        if self.xcor() < 330:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
    
    def go_left(self):
        if self.xcor() > -330:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())