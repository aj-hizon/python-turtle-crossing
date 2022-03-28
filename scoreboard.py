from turtle import Turtle
FONT = ("Arial", 15, "bold")
BIG_FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-230, 250)
        self.clear()
        self.write(f"LEVEL: {self.score}", align = "center", font = FONT)
    
    def score_up(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = BIG_FONT)
