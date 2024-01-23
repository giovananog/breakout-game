from turtle import Turtle
from random import randint, sample

# possible wall colors
COLORS = ['yellow', 'red', 'blue', 'green', 'violet', 'orange', 'pink', 'purple', 'cyan']


class Wall():

    def __init__(self):
        self.colors = sample(COLORS, 4)
        self.last_xpos = -360
        self.list = []
        self.last_xshape = 1
        self.walls = {c: [self.create_wall(c) for _ in range(10)] for c in self.colors}

    def create_wall(self, c):
        block = Turtle("square")
        block.color('white', c)
        block.shapesize(2, self.last_xshape, 2)
        block.penup()

        y = self.colors.index(c)

        if self.last_xpos < 300:
            block.goto(self.last_xpos + 10 + (2 * self.last_xshape) * 10, 260 - y * 60) 
        else: 
            self.last_xpos = -360
            self.last_xshape = 1
            block.goto(self.last_xpos + 10 + (2 * self.last_xshape) * 10, 260 - y * 60) 

        self.last_xpos = block.xcor() 
        self.last_xshape = randint(2, 4)
        self.list.append(block)



