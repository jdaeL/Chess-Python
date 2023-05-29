from chessPictures import *
from interpreter import draw

def join(p1, p2):
    """Returns a new Picture object by joining two pictures side by side."""
    joined_img = [row + p2_row for row, p2_row in zip(p1.img, p2.img)]
    return Picture(joined_img)


def draw_2x2_horses():
    black_horse = join(knight, knight)
    white_horse = join(knight, knight)

    top_row = join(black_horse, white_horse)
    bottom_row = join(black_horse, white_horse)

    full_board = join(top_row, bottom_row)

    draw(full_board)
   
draw_2x2_horses()
