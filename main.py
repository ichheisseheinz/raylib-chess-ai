from pyray import *
from raylib import *

from chess import *

SCREEN_DIM = 512

if __name__ == '__main__':
    init_window(SCREEN_DIM, SCREEN_DIM, 'chess')
    init_audio_device()

    chess = Chess(64)

    chess.populate_board()

    while not window_should_close():
        begin_drawing()

        clear_background(RAYWHITE)
        if is_mouse_button_pressed(0):
            chess.move()
        chess.draw_board()

        end_drawing()

    close_window()
    close_audio_device()
