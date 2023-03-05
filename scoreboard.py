from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 18, "bold"))

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 18, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=("Times New Roman", 18, "bold"))

    def count_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()








