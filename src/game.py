import sys

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Trendy Snake Game')
        self.clock = pygame.time.Clock()
        self.player = None
        self.npcs = []
        self.loaded = False

    def identify_player(self):
        for entity in self.npcs:
            if entity.is_player:
                self.player = entity
                break

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.player is not None and event.key == pygame.K_w:
                    self.player.move_up()
                elif event.key == pygame.K_a:
                    self.player.move_left()
                elif event.key == pygame.K_s:
                    self.player.move_down()
                elif event.key == pygame.K_d:
                    self.player.move_right()

    def load_game(self):
        # load game assets and display game interface
        print('Loading game...')
        self.loaded = True

    def start_game(self):
        # start the game and display the game interface
        print('Starting the game...')

    def run(self):
        self.load_game()
        while not self.loaded:
            pass
        while True:
            self.clock.tick(60)
            self.handle_input()
            self.identify_player()
            if self.loaded:
                self.start_game()
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
