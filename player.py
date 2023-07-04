from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.x_signs = []
        self.o_signs = []
        self.count_click = 0
        self.penup()
        self.hideturtle()

    def play(self, x, y):
        self.count_click += 1
        x_sign = Turtle("square")
        x_sign.hideturtle()
        x_sign.penup()
        o_sign = Turtle("square")
        o_sign.hideturtle()
        o_sign.penup()
        if -150 <= x <= -50:
            x = -100
        elif -50 < x <= 50:
            x = 0
        elif 50 < x <= 150:
            x = 100

        if -150 <= y <= -50:
            y = -100
        elif -50 < y <= 50:
            y = 0
        elif 50 < y <= 150:
            y = 100
        if self.count_click == 1 or self.count_click % 2 == 1:
            x_sign.goto(x, y)
            x_sign.color('#E966A0')
            x_sign.write('X', font=("Arial", 40, "bold"))
            self.x_signs.append((x_sign.xcor(), x_sign.ycor()))
            self.x_signs.sort()
        elif self.count_click % 2 == 0:
            o_sign.goto(x, y)
            o_sign.color('#2B2730')
            o_sign.write('O', font=("Arial", 40, "bold"))
            self.o_signs.append((o_sign.xcor(), o_sign.ycor()))
            self.o_signs.sort()
        else:
            print('Error')
