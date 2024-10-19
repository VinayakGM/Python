from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as f:
           self.high_score=int(f.read())
        self.color("blue")
        self.penup()
        self.goto(0,270)
        self.updateScoreBoard()
        self.hideturtle()

    
    def updateScoreBoard(self):
        self.clear()
        self.write(f"score : {self.score} Highest Score : {self.high_score}" ,align="center",font=("Arial",8,"normal"))
    
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as f:
                f.write(f"self.high_score")
        self.score=0
        self.updateScoreBoard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over" ,align="center",font=("Arial",16,"normal"))


        
    def IncreaseScore(self):
        self.score+=1
        self.updateScoreBoard()

