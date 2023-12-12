from Gameboard import Gameboard
import numpy as np

def init_board(gameboard: Gameboard):
    assert gameboard._gameboard.shape == (10, 10), "incorrect gameboard size"
    assert len(np.argwhere(gameboard._gameboard == -1).tolist()) == int(0.2 * 100), "incorrect number of obstacles"
    assert len(np.argwhere(gameboard._gameboard == -2).tolist()) == 1, "incorrect number of snake spaces"
    assert len(np.argwhere(gameboard._gameboard == 0).tolist()) == int(0.8 * 100) - 1, "incorrect number of free spaces"

if __name__ == "__main__":
    gameboard = Gameboard(10)
    init_board(gameboard)