from chessPictures import *
from interpreter import draw

# negative en las piezas
rockN = rock.negative()
knightN = knight.negative()
bishopN = bishop.negative()
queenN = queen.negative()
kingN = king.negative()
peonN = pawn.negative()
squareN = square.negative()

# Todas las piezas sobrepuestas con los squares
rockNsquare = square.sobreponer(rockN)
knightNsquare = square.sobreponer(knightN)
bishopNsquare = square.sobreponer(bishopN)
peonNsquare = square.sobreponer(peonN)
rockNsquareN = squareN.sobreponer(rockN)
knightNsquareN = squareN.sobreponer(knightN)
bishopNsquareN = squareN.sobreponer(bishopN)
peonNsquareN = squareN.sobreponer(peonN)
rockSquare = square.sobreponer(rock)
knightSquare = square.sobreponer(knight)
bishopSquare = square.sobreponer(bishop)
peonSquare = square.sobreponer(pawn)
rockSquareN = squareN.sobreponer(rock)
knightSquareN = squareN.sobreponer(knight)
bishopSquareN = squareN.sobreponer(bishop)
peonSquareN = squareN.sobreponer(pawn)
kingNSquare = square.sobreponer(kingN)
kingSquare = squareN.sobreponer(king)
queenNSquare = squareN.sobreponer(queenN)
queenSquare = square.sobreponer(queen)

# chessboard rows
row1 = rockNsquare.join(knightNsquareN).join(bishopNsquare).join(queenNSquare).join(kingNSquare).join(bishopNsquareN).join(knightNsquare).join(rockNsquareN)
row2 = (peonNsquareN.join(peonNsquare)).horizontalRepeat(4)
centro1 = square.join(squareN).horizontalRepeat(4)
centro2 = centro1.verticalMirror()
row3 = (peonSquare.join(peonSquareN)).horizontalRepeat(4)
row4 = rockSquareN.join(knightSquare).join(bishopSquareN).join(queenSquare).join(kingSquare).join(bishopSquare).join(knightSquareN).join(rockSquare)


# concatenacion & dibujo
chessboard = row1.up(row2).up(centro1.up(centro2).verticalRepeat(2)).up(row3).up(row4) 
draw(chessboard)