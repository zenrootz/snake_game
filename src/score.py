import pygame


class Score:
    def __init__(self):
        self.scores = []

    def update_score(self, new_score):
        self.scores.append(new_score)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:5]

    def display_scores(self):
        font = pygame.font.Font(None, 36)
        y = 10
        for score in self.scores:
            text = font.render("Score: " + str(score), 1, (10, 10, 10))
            self.screen.blit(text, (10, y))
            y += 40
