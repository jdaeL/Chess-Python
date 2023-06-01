from chessPictures import *
from interpreter import draw
from colors import inverter

board = (square.negative().join(square).horizontalRepeat(4))
draw(board)