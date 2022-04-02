from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.width(20)
        self.shapesize(stretch_wid=5, stretch_len=1.5)
        self.penup()
        self.goto(position)



    def go_up(self):
         new_y = self.ycor() + 20
         self.goto(self.xcor(), new_y)

    def go_down(self):
         new_y = self.ycor() - 20
         self.goto(self.xcor(), new_y)


#         self.another_paddle = []
#         self.head = self.another_paddle
#
#
#     def add_paddle(self):
#             new_paddle = Turtle("square")
#             new_paddle.color("white")
#             new_paddle.width(20)
#             new_paddle.shapesize(stretch_wid=5, stretch_len=1.5)
#             new_paddle.penup()
#             new_paddle.goto(x=350, y=0)
#             self.another_paddle.append(new_paddle)
#
#     def go_up(self):
#         new_y = self.head.ycor() + 20
#         self.head.goto(self.head.xcor(), new_y)
#
