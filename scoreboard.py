from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")
BIG_FONT = ("Courier", 60, "bold")


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Level: {self.score}", align = "center", font= FONT)

    def score_up(self):
        self.score += 1 
        self.update_scoreboard

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font= BIG_FONT)    
