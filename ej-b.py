from chessPictures import *
from interpreter import draw
from colors import inverter

white_knight = knight
black_knight = knight.negative()

# horizontalMirror() para modificar hacia donde miran los caballos
mirror_white_knight = white_knight.verticalMirror()
mirror_black_knight = black_knight.verticalMirror()

row1 = white_knight.join(black_knight)
row2 = mirror_black_knight.join(mirror_white_knight)
board = row1.under(row2)

draw(board)