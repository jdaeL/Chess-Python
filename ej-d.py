from chessPictures import *
from interpreter import draw
from colors import inverter

board = square.join(square.negative()).horizontalRepeat(4)
draw(board)