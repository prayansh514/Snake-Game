from turtle import Screen
import random
from snake import *
from food import Food
from scoreboard import Scoreboard

import time
# higher order functions are functions in which we can give any fnunctions as input as here in screen.onclick
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key = "Up",fun = snake.up)
screen.onkey(key = "Down",fun = snake.down)
screen.onkey(key = "Left",fun = snake.left)
screen.onkey(key = "Right",fun = snake.right)
screen.update()

while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision bw food
    dist  = food.distance(snake.snake[0])
    if(dist<15):
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # detect collision with wall

    x_cor = snake.snake[0].xcor()
    y_cor = snake.snake[0].ycor()
    if x_cor > 280 or x_cor<-300 or y_cor>280 or y_cor<-280:
        scoreboard.game_over()
        game_is_on = False


    # detect collision with tail
    for segment in snake.snake[1:]:
        if(snake.snake[0].distance(segment) < 10):
            game_is_on = False
            scoreboard.game_over()















screen.exitonclick()
