from turtle import Turtle

STARTING_POSITION = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.__snake_body: list[Turtle] = []
        self.__create_snake()
        self.__head: Turtle = self.__snake_body[0]

    def get_head(self):
        return self.__head

    def __create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        self.__snake_body.append(Turtle("square"))
        self.__snake_body[-1].penup()
        self.__snake_body[-1].color("white")
        self.__snake_body[-1].goto(position)

    def extend(self):
        self.add_segment(self.__snake_body[-1].position())

    def collision_with_tail(self):
        for segment in self.__snake_body[1:]:
            if self.__head.distance(segment) < 10:
                return True
        return False

    def reset(self):
        for segment in self.__snake_body:
            segment.hideturtle()
        self.__snake_body.clear()
        self.__create_snake()
        self.__head = self.__snake_body[0]

    def move(self):
        for i in range(len(self.__snake_body) - 1, 0, -1):
            self.__snake_body[i].goto(self.__snake_body[i - 1].xcor(), self.__snake_body[i - 1].ycor())
        self.__head.forward(MOVE_DISTANCE)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)

    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)
