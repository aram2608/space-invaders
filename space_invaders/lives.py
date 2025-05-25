import pygame
from pygame.sprite import Sprite

class Lives(Sprite):
    """A class to manage the ship."""

    def __init__(self, si_game): # self reference and reference to current instance of SpaceInvaders class
        """Initialize the lives and set starting position."""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = si_game.screen.get_rect()

       # Load the ship image and convert for better performance with transparency.
        image_path = '/Users/ja1473/space-invaders/assets/images/ship.png'
        self.image = pygame.image.load(image_path).convert_alpha() # converts transparents background
        self.rect = self.image.get_rect() # pygame treats all objects as rectangles

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
#
        # Store a float for the ships exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)