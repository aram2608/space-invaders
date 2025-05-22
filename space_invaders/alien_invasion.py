import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() # initializes background settings pygame needs to work properly
        self.clock = pygame.time.Clock() # create Clock instance

        # this makes the screen available to all methods in the class
        self.screen = pygame.display.set_mode((1200,800)) # tuple containing display size
        pygame.display.set_caption("Space Invaders")

        # Set background color, RBG values are used
        self.bg_color = (63, 0, 70) # Lower RBG values for darker colors

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()

            # A frame rate of 60 fps
            self.clock.tick(60)