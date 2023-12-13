import pygame
import constants as C
import numpy as np

class Display:
    def __init__(self, size: int, window: int = 400):
        self._size = size
        self._cell_size = int(window / size)

        pygame.init()
        self._screen = pygame.display.set_mode((window, window))
        self._clock = pygame.time.Clock()
        self._screen.fill("black")

    def render_gameboard(self, gameboard: np.ndarray) -> None:
        for row in range(self._size):
            for col in range(self._size):
                cell = gameboard[row, col]
                x = col * self._cell_size
                y = row * self._cell_size
                rect = pygame.Rect(x, y, self._cell_size, self._cell_size)
                colour = (255, 255, 255)
                border = 1

                if cell == C.SNAKE:
                    colour = (0, 255, 0)
                    border = 0
                elif cell in C.FOOD:
                    colour = (int(cell * 25.5), 0, 0)
                    border = 0
                elif cell == C.OBSTACLE:
                    border = 0

                pygame.draw.rect(self._screen, colour, rect, border)
        pygame.display.flip()
        self._clock.tick(1)
    
    def get_key_events(self) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return "QUIT"
                elif event.key in [pygame.K_w, pygame.K_UP]:
                    return "NORTH"
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    return "SOUTH"
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    return "EAST"
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    return "WEST"