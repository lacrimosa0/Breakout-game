from turtle import Turtle


POSITION = (0, 250)
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(POSITION)
		self.score = 0

	def show_score(self):
		self.write(f"points: {self.score}", align=ALIGNMENT, font=FONT)

	def score_up(self):
		self.score += 1
		self.write(f"points: {self.score}", align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.penup()
		self.goto(0, 0)
		self.write("Game Over!", align=ALIGNMENT, font=FONT)
