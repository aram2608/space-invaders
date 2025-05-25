"""Managing Statistics for Space Invaders."""

import pygame

class GameStats:
    """Track staistics for Space Invaders."""

    def __init__(self, si_game):
        """Initialize statistics."""
        self.settings = si_game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.alien_kills = 0
        self.ships_left = self.settings.ship_limit
        self.score = 0