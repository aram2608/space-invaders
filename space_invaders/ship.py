import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, si_game): # self reference and reference to current instance of SpaceInvaders class
        """Initialize the ship and set its starting position."""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

       # Load the ship image and convert for better performance with transparency.
        image_path = '/Users/ja1473/space-invaders/assets/images/placeholder.png'
        self.image = pygame.image.load(image_path).convert_alpha() # converts transparents background
        self.rect = self.image.get_rect() # pygame treats all objects as rectangles

        # Start each new ship at the bottom cetner of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)