from chessPictures import *
from interpreter import draw
from colors import inverter

squares_inv = (square.negative()).join(square)

board = squares_inv.join(squares_inv).join(squares_inv.join(squares_inv))
draw(board)