from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=4, stretch_len=1)
		self.penup()
		self.setheading(90)
		self.goto(position)

	def go_left(self):
		new_x = self.xcor() - 20
		self.goto(new_x, self.ycor())

	def go_right(self):
		new_x = self.xcor() + 20
		self.goto(new_x, self.ycor())