from chessPictures import *
from interpreter import draw
from colors import inverter

squares = square.join(square.negative())

board = squares.join(squares).join(squares.join(squares))
draw(board)