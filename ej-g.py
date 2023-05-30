from chessPictures import *
from interpreter import draw
from colors import inverter

squares = square.join(square.negative())
squares_inv = (square.negative()).join(square)
row1 = squares.join(squares).join(squares.join(squares))
row2 = squares_inv.join(squares_inv).join(squares_inv.join(squares_inv))
set_of_rows = row1.under(row2)
rows = set_of_rows.under(set_of_rows)

# whole board 
board = rows.under(rows)

# faltara definir las piezas con  horizontalRepeat(self, n): y verticalRepeat(self, n):
board_completed = 0

draw(board_completed)
