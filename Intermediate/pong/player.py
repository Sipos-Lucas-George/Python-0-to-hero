from turtle import Turtle

MOVEMENT = 20


class Player(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos_x, pos_y)

    def up(self):
        new_y = self.ycor() + MOVEMENT
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVEMENT
        if new_y > -250:
            self.goto(self.xcor(), new_y)
