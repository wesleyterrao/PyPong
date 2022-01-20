from turtle import Turtle

# POSITION_R_PADDLE = (350, 0)
# POSITION_L_PADDLE = (-350, 0)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setposition(position)

    def up(self):
        new_y = self.ycor() + 60
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 60
        self.goto(self.xcor(), new_y)
