import sys
import logging

import pygame

logging.basicConfig(filename='src/error_log.txt', level=logging.ERROR)


from src.level import Level  # Import the Level class

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Trendy Snake Game')
        self.clock = pygame.time.Clock()
        self.player = None
        self.npcs = []
        self.level = Level()  # Create a Level instance
        self.level.generate_level()  # Generate the first level
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
                if self.player is not None:
                    if event.key == pygame.K_w:
                        self.player.move_up()
                    elif event.key == pygame.K_a:
                        self.player.move_left()
                    elif event.key == pygame.K_s:
                        self.player.move_down()
                    elif event.key == pygame.K_d:
                        self.player.move_right()
                # Add more input handlers if needed

    def load_game(self):
        try:
            # load game assets and display game interface
            print('Loading game...')
            # Example asset loading (this should be adjusted for actual assets)
            # self.player_sprite = pygame.image.load('assets/player.png').convert_alpha()
            # Check if the player sprite is not loaded
            # if not self.player_sprite:
            #     raise Exception('Failed to load player sprite')
            self.loaded = True
        except Exception as e:
            logging.error(f'Error loading game assets: {e}')
            self.loaded = False
            pygame.quit()
            sys.exit()

    def start_game(self):
        # start the game and display the game interface
        print('Starting the game...')

    def run(self):
        self.load_game()
        self.load_game()
        # Game main loop
        while True:
            self.clock.tick(60)
            self.handle_input()

            if not self.loaded:
                continue  # Skip the rest of the loop if the game has not loaded

            # Perform game state updates
            # self.update_game_state()

            # Perform game rendering
            # self.render()

            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
