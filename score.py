from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.scorenum = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("White")
        self.write(arg=f"Score: {self.scorenum}", move=False, align="center", font=("Courier", 18, "bold"))
        self.newscore()

    def newscore(self):
        self.clear()
        self.write(arg=f"Score: {self.scorenum}", move=False, align="center", font=("Courier", 18, "bold"))
        self.scorenum += 1

    def gameover(self):
        self.goto(0,0)
        self.write(arg=f"Game Over", move=False, align="center", font=("Courier", 20, "bold"))