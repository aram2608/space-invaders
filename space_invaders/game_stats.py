"""Managing Statistics for Space Invaders."""

import pygame

class GameStats:
    """Track staistics for Space Invaders."""

    def __init__(self, si_game):
        """Initialize statistics."""
        self.settings = si_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit

class GameOver:
    """An image to print once a game has ended."""
    def __init__(self, si_game):
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = si_game.settings

        # Load image
        image_path = '/Users/ja1473/space-invaders/assets/images/game_over_placeholder.png'
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        """Load Game Over image to screen."""
        self.screen.blit(self.image, self.rect)