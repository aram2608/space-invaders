import pygame

from space_invaders.settings import Settings

class Ship:
    """A class to manage the ship."""

    def __init__(self, si_game): # self reference and reference to current instance of SpaceInvaders class
        """Initialize the ship and set its starting position."""
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

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update position given the movement flags."""

        if self.moving_right and self.rect.right < self.screen_rect.right: # Sets right screen boundary
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left: # Sets left screen boundary
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top: # Sets top screen boundary
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom: # Sets bottom screen boundary
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)