import pygame


class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 'UP'

    def move_up(self):
        self.direction = 'UP'

    def move_down(self):
        self.direction = 'DOWN'

    def move_left(self):
        self.direction = 'LEFT'

    def move_right(self):
        self.direction = 'RIGHT'

    def update(self):
        if self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed
        elif self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'RIGHT':
            self.x += self.speed
