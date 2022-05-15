from turtle import Turtle


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("gray")
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.move_speed = 0.05
		self.goto(0, 0)

	def refresh(self):
		self.x_move = 10
		self.y_move = 10
		self.goto(0, 0)
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def move_ball(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_down(self):
		self.y_move *= -1
		if self.move_speed != 0.07:
			self.move_speed -= 0.002

	def bounce_up(self):
		self.x_move *= -1

	def bounce_paddle(self):
		self.y_move *= -1


