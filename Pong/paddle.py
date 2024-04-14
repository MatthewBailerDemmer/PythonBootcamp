from turtle import Turtle
class Paddle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)  # Turtle starts with 20 by 20 size
        self.penup()
        self.color("white")
        self.goto(position)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > - 240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)