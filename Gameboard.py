import constants as C
import numpy as np
from random import choice, sample
from helpers import manhattan
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
    
    def get_state(self) -> np.ndarray:
        """
        Returns a copy of the gameboard in its current state
        """
        return {
            "gameboard": self._gameboard.copy(),
            "snake": self._snake.copy(),
            "size": self._size
        }
    
    def get_gameboard(self) -> np.ndarray:
        """
        Returns a copy of the gameboard
        """
        return self._gameboard.copy()
    
    def _render_snake(self, prev: Tuple[int, int], next: Tuple[int, int]) -> None:
        if prev: self._gameboard[prev] = 0
        self._gameboard[next] = C.SNAKE
    
    def move_snake(self, direction: str) -> int:
        """
        Moves snake on gameboard, returns True if snake hit obstacle, otherwise False
        """
        assert direction in C.DIRECTIONS.keys(), "direction not in list"

        next = tuple(map(sum, zip(C.DIRECTIONS[direction], self._snake[0])))
        if (any([n < 0 or n >= self._size for n in next])
            or manhattan(self._snake[0], next) > 1 or self._gameboard[next] < 0):
            return C.QUIT
        cell = self._gameboard[next]
        self._snake.insert(0, next)
        prev = self._snake.pop() if cell < 1 else None
        self._render_snake(prev, next)
        return cell