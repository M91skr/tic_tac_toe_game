from turtle import Turtle


class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#6554AF')
        self.penup()

    def description_writing(self):
        self.goto(-200, 200)
        self.write('Starts the game with player x.\nPlayer x clicks on a cell.\nThen player o plays.', font=("Arial", 20, "normal"))

    def board_drawing(self):
        self.goto(-150, 50)
        self.pensize(10)
        self.pendown()
        self.right(0)
        self.forward(300)
        self.penup()
        self.goto(150, -50)
        self.right(180)
        self.pendown()
        self.forward(300)
        self.penup()
        self.goto(-50, -150)
        self.right(90)
        self.pendown()
        self.forward(300)
        self.penup()
        self.goto(50, 150)
        self.pendown()
        self.forward(-300)
        self.penup()
        self.hideturtle()


    def winner_Announcing(self, w ):
        self.goto(-200, -200)
        self.write(f"{w} won!", font=("Arial", 20, "bold"))

