import random
import logging
import os

if not os.path.exists('src/error_log.txt'):
    open('src/error_log.txt', 'w').close()

import pygame

logging.basicConfig(filename='src/error_log.txt', level=logging.ERROR)


class Level:
    def __init__(self):
        self.level_number = 1
        self.levels = []

    def generate_level(self):
        try:
            level = []
            for i in range(self.level_number * 10):  # Increase the number of obstacles with the level number
                obstacle = pygame.Rect(random.randint(0, 800), random.randint(0, 600), 50, 50)
                level.append(obstacle)
            self.levels.append(level)
        except Exception as e:
            logging.error(f'Error generating level: {e}')
            return False
        return True

    def increase_difficulty(self):
        self.level_number += 1
        self.generate_level()

    def get_current_level(self):
        return self.levels[self.level_number - 1]
            print(f'Error increasing difficulty: {e}')
            return False
        return True

    def get_current_level(self):
        return self.levels[self.level_number - 1]
    def get_current_level(self):
        try:
            return self.levels[self.level_number - 1]
        except IndexError:
            logging.error(f'Error: Level {self.level_number} not found')
            return None
        except Exception as e:
            logging.error(f'Unexpected error getting current level: {e}')
            return None
