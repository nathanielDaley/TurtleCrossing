from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_X_POSITION = -290
SCORE_Y_POSITION = 260

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.draw_score()

    def draw_score(self):
        self.goto(SCORE_X_POSITION, SCORE_Y_POSITION)
        self.write(f"Level: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.draw_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)