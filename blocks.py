from turtle import Turtle


class Blocks(Turtle):
	def __init__(self):
		super().__init__()
		self.red_blocks = []
		self.orange_blocks = []
		self.blue_blocks = []
		self.green_blocks = []
		self.all_blocks = []
		self.penup()

	def create_blocks(self):
		for i in range(11):
			red_block = Turtle("square")
			red_block.color("red")
			red_block.penup()
			red_block.setheading(90)
			red_block.shapesize(stretch_wid=4, stretch_len=1)
			self.red_blocks.append(red_block)
			self.all_blocks.append(red_block)

		for i in range(11):
			orange_block = Turtle("square")
			orange_block.color("orange")
			orange_block.penup()
			orange_block.setheading(90)
			orange_block.shapesize(stretch_wid=4, stretch_len=1)
			self.orange_blocks.append(orange_block)
			self.all_blocks.append(orange_block)

		for i in range(11):
			blue_block = Turtle("square")
			blue_block.color("blue")
			blue_block.penup()
			blue_block.setheading(90)
			blue_block.shapesize(stretch_wid=4, stretch_len=1)
			self.blue_blocks.append(blue_block)
			self.all_blocks.append(blue_block)

		for i in range(11):
			green_block = Turtle("square")
			green_block.color("green")
			green_block.penup()
			green_block.setheading(90)
			green_block.shapesize(stretch_wid=4, stretch_len=1)
			self.green_blocks.append(green_block)
			self.all_blocks.append(green_block)

	def red_loc(self):
		starting_xcor = -455
		starting_ycor = 200
		for i in range(11):
			self.red_blocks[i].goto(starting_xcor, starting_ycor)
			starting_xcor += 90

	def orange_loc(self):
		starting_xcor = -455
		starting_ycor = 160
		for i in range(11):
			self.orange_blocks[i].goto(starting_xcor, starting_ycor)
			starting_xcor += 90

	def blue_loc(self):
		starting_xcor = -455
		starting_ycor = 120
		for i in range(11):
			self.blue_blocks[i].goto(starting_xcor, starting_ycor)
			starting_xcor += 90

	def green_loc(self):
		starting_xcor = -455
		starting_ycor = 80
		for i in range(11):
			self.green_blocks[i].goto(starting_xcor, starting_ycor)
			starting_xcor += 90

