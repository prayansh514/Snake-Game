from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("score.txt",encoding="utf-8") as file:
            contents = file.read()
            self.high_score = int(contents)
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.display()

    def update_score(self):
        self.score+=1
        self.clear()
        self.display()

    def display(self):
        self.write(f"Score : {self.score} High Score : {self.high_score}",False,"center",font=('Arial', 18, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER ", False, "center", font=('Arial', 18, 'normal'))
    #
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt",mode = "w") as file:
                file.write(str(self.high_score))
        self.score = 0

