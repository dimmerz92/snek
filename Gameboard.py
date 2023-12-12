import constants as C
import numpy as np
from random import choice, sample
from typing import List, Tuple

class Gameboard:
    def __init__(self, size: int):
        self._size: int = size
        self._gameboard: np.ndarray = Gameboard._init_gameboard(size)
        self._snake: List[Tuple[int, int]] = self._random_snake()

    def _init_gameboard(size: int) -> np.ndarray:
        gameboard = np.zeros((size, size), dtype=int)
        obstacles = sample(Gameboard.get_empty(gameboard), k=int(0.2 * size**2))
        for coord in obstacles: gameboard[tuple(coord)] = C.OBSTACLE

        np.argwhere(gameboard == 0)

        return gameboard
    
    def _random_snake(self) -> List[Tuple[int, int]]:
        coord = choice(Gameboard.get_empty(self._gameboard))
        self._gameboard[coord] = C.SNAKE
        return [coord]
    
    def get_empty(gameboard: np.ndarray) -> List[Tuple[int, int]]:
        """
        Returns a list of integer 2-tuple coordinates of empty cells
        """
        return [tuple(coord) for coord in np.argwhere(gameboard == 0).tolist()]