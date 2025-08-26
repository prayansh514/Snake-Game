from turtle import Turtle,Screen
import random
class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            self.add_segment(0 - 20 * i, 0)


    def add_segment(self,x_cor,y_cor):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x_cor,y_cor)
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].xcor(),self.snake[-1].ycor())

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            prev_x_cor = self.snake[i - 1].xcor()
            prev_y_cor = self.snake[i - 1].ycor()
            self.snake[i].goto(prev_x_cor, prev_y_cor)

        self.snake[0].forward(20)
    def up(self):
        if(self.snake[0].heading()!=270):
            self.snake[0].setheading(90)
    def down(self):
        if (self.snake[0].heading() != 90):
            self.snake[0].setheading(270)
    def right(self):
        if (self.snake[0].heading() != 180):
            self.snake[0].setheading(0)
    def left(self):
        if (self.snake[0].heading() != 0):
            self.snake[0].setheading(180)

    def reset(self):
        for segment in self.snake:
            segment.goto(-900,-900)

        self.snake.clear()
        for i in range(3):
            self.add_segment(0 - 20 * i, 0)










