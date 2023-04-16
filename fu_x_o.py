from turtle import Turtle, bgcolor

turtle = Turtle()
count = 0
pieces = ["","","","","","","","",""]
nextTurn = "X"
squarelist = []


turtle.speed(0)
turtle.hideturtle()
turtle.pensize(20)


#function for drawing x
def for_x(x,y):
    turtle.color('red')
    turtle.up()
    turtle.goto(x+20,y-20)
    turtle.setheading(-45)
    turtle.down()
    turtle.forward(225)
    turtle.up()
    turtle.goto(x+180,y-20)
    turtle.setheading(-135)
    turtle.down()
    turtle.forward(225)
    turtle.up()

#function draw o
def for_o(x,y):
    turtle.color('green')
    turtle.up()
    turtle.goto(x+100,y-180)
    turtle.setheading(0)
    turtle.down()
    turtle.circle(80)
    turtle.up()

#if clicked on screen this function will work
def clicked(x,y):
    global nextTurn,pieces
    column = (x + 300) // 200
    row = (-y + 300)  // 200
    square = column + row*3
    square = int(square)
    pieces[square] = nextTurn

    if nextTurn == "X":
        nextTurn = "O"
    else:
        nextTurn = "X"

    if not square in squarelist:
        squarelist.append(square)
        draw_x_o(pieces)
        check_apple()

#for drawing x and o
def draw_x_o(pieces):
    if count < 10:
        x = -300
        y = 300
        for piece in pieces:
            if piece == "X":
                for_x(x,y)
            elif piece == "O":
                for_o(x,y)
            x = x + 200
            if x > 100:
                x = -300
                y = y - 200
    for_winner()

pearl = ['X','O']
final = 0
apple = 0

def check_apple():
    if "X" in pieces or "O" in pieces:
        global apple
        apple += 1

# check winner
def for_winner():

    for j in pearl:

        if j == pieces[0] == pieces[1] == pieces[2]:
            for_winners(j)
            game = 'pause'       
            
        elif j == pieces[3] == pieces[4] == pieces[5]:
            for_winners(j)
            game = 'pause'   

        elif j == pieces[6] == pieces[7] == pieces[8]:
            for_winners(j)
            game = 'pause'     

        elif j == pieces[0] == pieces[3] == pieces[6]:
            for_winners(j)  
            game = 'pause'     

        elif j == pieces[1] == pieces[4] == pieces[7]:
            for_winners(j)  
            game = 'pause'   

        elif j == pieces[2] == pieces[5] == pieces[8]:
            for_winners(j) 
            game = 'pause'    

        elif j == pieces[0] == pieces[4] == pieces[8]:
            for_winners(j)  
            game = 'pause'   

        elif j == pieces[2] == pieces[4] == pieces[6]:
            for_winners(j) 
            game = 'pause'

        if apple == 8:
            for_draw()
            game = 'pause'


# print winner on screen
def for_winners(winne):
    turtle.clear()
    bgcolor('white')
    turtle.color('black')
    turtle.goto(-100,0)
    turtle.write(f"Winner is {winne}", font=("Arial", 30, "normal"))

def for_draw():
    turtle.clear()
    bgcolor('white')
    turtle.color('black')
    turtle.goto(-50,0)
    turtle.write(f"Draw", font=("Arial", 30, "normal"))