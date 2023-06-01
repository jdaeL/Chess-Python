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

# 
chessboard = 0

# 
draw(chessboard)