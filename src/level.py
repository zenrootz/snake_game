import random

import pygame


class Level:
    def __init__(self):
        self.level_number = 1
        self.levels = []

    def generate_level(self):
        level = []
        for i in range(self.level_number):
            obstacle = pygame.Rect(random.randint(0, 800), random.randint(0, 600), 50, 50)
            level.append(obstacle)
        self.levels.append(level)

    def increase_difficulty(self):
        self.level_number += 1
        self.generate_level()

    def get_current_level(self):
        return self.levels[self.level_number - 1]
