"""Module to render title screens."""

import pygame

class GameOver:
    """An image to print once a game has ended."""
    def __init__(self, si_game):
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load image
        image_path = '/Users/ja1473/space-invaders/assets/images/game_over_placeholder.png'
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

        # Set position
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Load Game Over image to screen."""
        self.screen.blit(self.image, self.rect)

class GameStart:
    """An image to print at start of the game."""
    def __init__(self, si_game):
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load image
        image_path = '/Users/ja1473/space-invaders/assets/images/game_start_placeholder.png'
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

        # Set postion
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Load start game image."""
        self.screen.blit(self.image, self.rect)