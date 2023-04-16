from turtle import *
from draw_lines import board
from fu_x_o import *

#for screen
setup(width=600, height=600)
title('Tic,Tac,Toe')
bgcolor('black')

#call function for draw board with grip lines
a = board()
a.draw_lines()

#call function for draw o and x when click
onscreenclick(clicked)
done()