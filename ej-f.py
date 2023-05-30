from chessPictures import *
from interpreter import draw
from colors import inverter

squares = square.join(square.negative())
squares_inv = (square.negative()).join(square)

row1 = squares.join(squares).join(squares.join(squares))
row2 = squares_inv.join(squares_inv).join(squares_inv.join(squares_inv))

set_of_rows = row1.under(row2)

rows = set_of_rows.under(set_of_rows)
board = rows.under(rows)
draw(board)

