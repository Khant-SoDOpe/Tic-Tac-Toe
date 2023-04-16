from turtle import Turtle
turtle = Turtle()

class board:

    def __init__(self) -> None:
        self.position_list = [(-300,100), (-300,-100), (-100,300), (100,300)]
        self.degree = [0,0,90,0]
        turtle.speed(0)
        turtle.pensize(20)
    
    #draw lines on screen
    def draw_lines(self):
        for i in range(4):
            turtle.speed(0)
            turtle.penup()
            turtle.goto(self.position_list[i])
            turtle.pendown()
            turtle.color('white')
            turtle.right(self.degree[i])
            turtle.forward(600)