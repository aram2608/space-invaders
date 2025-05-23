import sys

import pygame

from space_invaders.settings import Settings
from space_invaders.ship import Ship

class SpaceInvaders:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() # initializes background settings pygame needs to work properly
        self.clock = pygame.time.Clock() # create Clock instance
        self.settings = Settings()

        # this makes the screen available to all methods in the class
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Space Invaders")

        # Initializes a Ship class instance with Space Invaders as the reference
        # I believe this is known as recursion
        self.ship = Ship(self)

        # Set background color, RBG values are used
        self.bg_color = (63, 0, 70) # Lower RBG values for darker colors

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # A frame rate of 60 fps
            self.clock.tick(60)

    # Helper methods use the following syntax _method_name, underscore goes first.
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
    # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
    # Make the most recently drawn screen visible
        pygame.display.flip()