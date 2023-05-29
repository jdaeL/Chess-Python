from chessPictures import *
from interpreter import draw
from colors import inverter


def draw_2x2_horses():
    row1 = knight.join(knight)
    row2 = knight.join(knight)
    board = row1.under(row2) 

    draw(board)
   
draw_2x2_horses()