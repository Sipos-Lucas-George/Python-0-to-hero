from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto Mono", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__player_one_score = 0
        self.__player_two_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.__player_one_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.__player_two_score, align=ALIGNMENT, font=FONT)

    def increase_player_one(self):
        self.__player_one_score += 1
        self.update_scoreboard()

    def increase_player_two(self):
        self.__player_two_score += 1
        self.update_scoreboard()
