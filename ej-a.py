from chessPictures import *
from interpreter import draw
from colors import inverter

white_knight = knight
black_knight = knight.negative()

row1 = white_knight.join(black_knight)
row2 = black_knight.join(white_knight)
board = row1.under(row2)

draw(board)