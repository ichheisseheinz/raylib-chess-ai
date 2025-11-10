from pyray import *
from raylib import *

from piece import Piece

class Chess:
    def __init__(self, cell_size: int):
        self.cell_size: int = cell_size
        self.board: list = [0] * 64

        self.index, self.new_index = 0, 0
        self.moving = False
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
        
        if self.moving:
            draw_rectangle_lines_ex(
                Rectangle((self.index % 8) * self.cell_size, (self.index // 8) * self.cell_size, self.cell_size, self.cell_size),
                5,
                YELLOW
            )

        # Pieces
        for index, piece in enumerate(self.board):
            color = Piece.WHITE.value if piece & 8 == 8 else Piece.BLACK.value

            for type in [Piece.ROOK.value, Piece.KNIGHT.value, Piece.BISHOP.value, Piece.KING.value, Piece.QUEEN.value, Piece.PAWN.value]:
                if piece & type == type:
                    draw_texture_pro(
                        self.image,
                        self.image_crops[color | type],
                        Rectangle((index % 8) * self.cell_size, (index // 8) * self.cell_size, self.cell_size, self.cell_size),
                        Vector2(0, 0),
                        0,
                        WHITE
                        )
                    break
    
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
        
        self.board.reverse()
        
        self.white_move = fen_board[1] == 'w'
    
    def move(self):
        if not self.moving:
            self.index = (get_mouse_y() // self.cell_size) * 8 + (get_mouse_x() // self.cell_size)
            if self.board[self.index] != Piece.NONE.value:
                self.moving = True
        else:
            self.new_index = (get_mouse_y() // self.cell_size) * 8 + (get_mouse_x() // self.cell_size)
            self.moving = False

            if self.new_index != self.index and self.board[self.new_index] == Piece.NONE.value:
                self.board[self.new_index] = self.board[self.index]
                self.board[self.index] = Piece.NONE.value
            
                self.index, self.new_index = 0, 0
                self.white_move = not self.white_move
