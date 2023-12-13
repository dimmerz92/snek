from Gameboard import Gameboard
import numpy as np

def init_board(gameboard: Gameboard):
    assert gameboard._gameboard.shape == (10, 10), "incorrect gameboard size"
    assert len(np.argwhere(gameboard._gameboard == -1).tolist()) == int(0.2 * 100), "incorrect number of obstacles"
    assert len(np.argwhere(gameboard._gameboard == -2).tolist()) == 1, "incorrect number of snake spaces"
    assert len(np.argwhere(gameboard._gameboard == 0).tolist()) == int(0.8 * 100) - 1, "incorrect number of free spaces"

def check_state(gameboard: Gameboard):
    state = gameboard.get_state()
    assert isinstance(state["gameboard"], np.ndarray), "gameboard is not an ndarray"
    assert isinstance(state["snake"], list) and len(state["snake"]) == 1, "snake is not a list of length 1"
    assert state["size"] == 10, "size not correct in state"

def check_movement(gameboard: Gameboard):
    moved = gameboard.move_snake("NORTH", True)
    assert isinstance(moved, bool), "Not a valid movement"
    assert len(gameboard._snake) == 2, "Snake did not grow after eating"

if __name__ == "__main__":
    gameboard = Gameboard(10)
    init_board(gameboard)
    check_state(gameboard)
    check_movement(gameboard)