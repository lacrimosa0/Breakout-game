from turtle import *
from paddle import Paddle
from blocks import Blocks
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)  # TURN OFF THE ANIMATION


paddle = Paddle((0, -270))
blocks = Blocks()
ball = Ball()
scoreboard = ScoreBoard()

blocks.create_blocks()
scoreboard.show_score()


blocks.red_loc()
blocks.orange_loc()
blocks.blue_loc()
blocks.green_loc()


screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

screen.update()

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(ball.move_speed)
	ball.move_ball()

	# if ball hits a block
	for block in blocks.all_blocks:
		if ball.distance(block) < 50 and ball.xcor() > 0:
			block.goto(1000, 600)
			scoreboard.clear()
			scoreboard.score_up()
			ball.bounce_down()
		if ball.distance(block) < 50 and ball.xcor() < 0:
			hit_block = block
			block.goto(1000, 600)
			scoreboard.clear()
			scoreboard.score_up()
			ball.bounce_down()

	# if ball hits the paddle
	if ball.distance(paddle) < 40 and ball.xcor() > 0:
		ball.bounce_paddle()

	if ball.distance(paddle) < 40 and ball.xcor() < 0:
		ball.bounce_paddle()

	# if ball hits right wall
	if ball.xcor() > 480:
		ball.bounce_up()

	# if ball hits left wall
	if ball.xcor() < -480:
		ball.bounce_up()

	if ball.ycor() > 260:
		ball.bounce_down()

	# die
	if ball.ycor() < -300:
		game_is_on = False
		scoreboard.game_over()


screen.exitonclick()
