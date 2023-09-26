from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.__x_move = 10
        self.__y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.__x_move, self.ycor() + self.__y_move)

    def bounce_y(self):
        self.__y_move *= -1

    def bounce_x(self):
        self.__x_move *= -1
        self.move_speed *= 0.90

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.__x_move *= -1
