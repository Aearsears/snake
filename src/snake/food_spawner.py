import random
import pygame
import logging


class FoodSpawner:
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.food = []

    def spawn_food(self):
        # Spawn food at a random position on the grid
        x = random.randint(self.grid[0][0], self.grid[1][0])
        y = random.randint(self.grid[0][1], self.grid[3][1])
        rect = pygame.draw.rect(self.screen, "yellow", (x, y, 10, 10))
        logging.debug(f"Spawned food at {rect.topleft}")
        self.food.append(rect)
        return rect

    def draw_food(self):
        for f in self.food:
            pygame.draw.rect(self.screen, "yellow", f)
