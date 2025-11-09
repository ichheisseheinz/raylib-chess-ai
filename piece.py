from enum import Enum

class Piece(Enum):
    NONE = 0
    PAWN = 1
    KING = 2
    KNIGHT = 3
    BISHOP = 4
    ROOK = 5
    QUEEN = 6
    
    WHITE = 8
    BLACK = 16
