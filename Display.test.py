import sys
import numpy as np
from Display import Display

def render_board(display: Display, board: np.ndarray):
    iter = 0
    while iter < 100:
        key = display.get_key_events()
        if key == "QUIT":
            sys.exit()
        display.render_gameboard(board)
        iter += 1

if __name__ == "__main__":
    display = Display(10)
    board = np.random.randint(-2, 11, size=(10, 10))
    render_board(display, board)