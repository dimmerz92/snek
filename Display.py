import pygame
import constants as C
import numpy as np

class Display:
    def __init__(self, size: int, window: int = 400):
        self._size = size
        self._cell_size = int(window / size)

        pygame.init()
        pygame.display.set_caption("SNEK!!11!1!one!")
        self._screen = pygame.display.set_mode((window, window + 100))
        self._clock = pygame.time.Clock()
        self._screen.fill("black")

    def render_score(self, text: str) -> None:
        font = pygame.font.SysFont("monospace", 20)
        size = font.size(text)
        display = font.render(text, True, (255, 255, 255))
        self._screen.blit(display, ((400 - size[0])/2, 50))
        pygame.display.flip()

    def render_gameboard(self, gameboard: np.ndarray) -> None:
        self._screen.fill("black")
        for row in range(self._size):
            for col in range(self._size):
                cell = gameboard[row, col]
                x = col * self._cell_size
                y = row * self._cell_size + 100
                rect = pygame.Rect(x, y, self._cell_size, self._cell_size)
                colour = (255, 255, 255)
                border = 1

                if cell == C.SNAKE:
                    colour = (0, 255, 0)
                    border = 0
                elif cell in C.FOOD:
                    colour = (int(cell * 15.5) + 100, 0, 0)
                    border = 0
                elif cell == C.OBSTACLE:
                    border = 0

                pygame.draw.rect(self._screen, colour, rect, border)
        self._clock.tick(3)
    
    def get_key_events(self) -> str | None:
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
        return None