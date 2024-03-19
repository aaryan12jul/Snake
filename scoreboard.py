from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        try:
            with open("highscore.txt", mode='r') as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            with open("highscore.txt", mode='w') as file:
                self.highscore = 0
                file.write(str(self.highscore))
        self.score = 0
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(0, 250)
        self.update_score()

    def update_score(self):    
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()