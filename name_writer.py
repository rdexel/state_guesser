from turtle import Turtle


class WriteName(Turtle):
    def __init__(self, coordinates, answer):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(coordinates)
        self.write(arg=answer, move=False, align='center', font=('Arial', 12, 'normal'))

