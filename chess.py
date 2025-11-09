from pyray import *
from raylib import *

from piece import Piece

class Chess:
    def __init__(self, cell_size: int):
        self.cell_size: int = cell_size
        self.board: list = [0] * 64
        self.white_move: bool = True

        image = load_image('assets/chesspieces.png')
        self.image: Texture2D = load_texture_from_image(image)
        unload_image(image)
        self.image_crops: dict = self.load_crops()
    
    def load_crops(self) -> dict:
        piece_order = [Piece.ROOK.value, Piece.KNIGHT.value, Piece.BISHOP.value, Piece.KING.value, Piece.QUEEN.value, Piece.PAWN.value]
        textures = {}

        # Load white crop rects
        for row in range(6):
            key = piece_order[row] | Piece.WHITE.value

            textures[key] = Rectangle(row * 16, 0, 16, 16)

        # Load black crop rects
        for row in range(6):
            key = piece_order[row] | Piece.BLACK.value

            textures[key] = Rectangle(row * 16, 16, 16, 16)

        return textures
        
    def draw_board(self):
        # Board
        for i in range(8):
            for j in range(8):
                light = (i + j) % 2 != 0

                draw_rectangle(
                    i * self.cell_size,
                    j * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    BEIGE if light else DARKBROWN
                )

        # Pieces
        for index, piece in enumerate(reversed(self.board)):
            # TODO: replace if statements with more robust checking
            if piece == Piece.WHITE.value | Piece.ROOK.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.WHITE.value | Piece.ROOK.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.WHITE.value | Piece.KNIGHT.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.WHITE.value | Piece.KNIGHT.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.WHITE.value | Piece.BISHOP.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.WHITE.value | Piece.BISHOP.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.WHITE.value | Piece.KING.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.WHITE.value | Piece.KING.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.WHITE.value | Piece.QUEEN.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.WHITE.value | Piece.QUEEN.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.WHITE.value | Piece.PAWN.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.WHITE.value | Piece.PAWN.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.BLACK.value | Piece.ROOK.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.BLACK.value | Piece.ROOK.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.BLACK.value | Piece.KNIGHT.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.BLACK.value | Piece.KNIGHT.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.BLACK.value | Piece.BISHOP.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.BLACK.value | Piece.BISHOP.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.BLACK.value | Piece.KING.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.BLACK.value | Piece.KING.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.BLACK.value | Piece.QUEEN.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.BLACK.value | Piece.QUEEN.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
            elif piece == Piece.BLACK.value | Piece.PAWN.value:
                draw_texture_pro(
                    self.image,
                    self.image_crops[Piece.BLACK.value | Piece.PAWN.value],
                    Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                    Vector2(0, 0),
                    0,
                    WHITE
                    )
    
    def populate_board(self, fen='rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR w'):
        """
        Populates the board from a string in FEN notation
        If no FEN string is provided, the default start for a chessboard is used
        rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR w

        Algorithm from Sebastian Lague's video on creating a chess AI
        https://youtu.be/U4ogK0MIzqk?si=GIMPM4ghqcwgsYWC
        """

        piece_map = {
            'r' : Piece.ROOK.value,
            'n' : Piece.KNIGHT.value,
            'b' : Piece.BISHOP.value,
            'k' : Piece.KING.value,
            'q' : Piece.QUEEN.value,
            'p' : Piece.PAWN.value
        }

        fen_board = fen.split(' ')
        file = 0
        rank = 7

        for symbol in fen_board[0]:
            if symbol == '/':
                file = 0
                rank -= 1
            else:
                if symbol.isdigit():
                    file += int(symbol)
                else:
                    color = Piece.WHITE.value if symbol.isupper() else Piece.BLACK.value
                    type = piece_map[symbol.lower()]
                    self.board[rank * 8 + file] = color | type
                    file += 1
        
        self.white_move = fen_board[1] == 'w'
