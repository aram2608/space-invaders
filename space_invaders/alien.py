import pygame

class Alien:
    """A class to manage aliens."""

    def __init__(self, si_game): # self reference and reference to current instance of SpaceInvaders class
        """Initialize the alien and set its starting position."""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

       # Load the ship image and convert for better performance with transparency.
        image_path = '/Users/ja1473/space-invaders/assets/images/alien.png'
        self.image = pygame.image.load(image_path).convert_alpha() # converts transparents background
        self.rect = self.image.get_rect() # pygame treats all objects as rectangles

        # Start each new alien at the mid top of screen
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

class BossAlien:
    """A class to manage the boss type alien."""

    def __init__(self, si_game): # self reference and reference to current instance of SpaceInvaders class
        """Initialize the boss alien and set its starting position."""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

       # Load the ship image and convert for better performance with transparency.
        image_path = '/Users/ja1473/space-invaders/assets/images/boss_alien.png'
        self.image = pygame.image.load(image_path).convert_alpha() # converts transparents background
        self.rect = self.image.get_rect() # pygame treats all objects as rectangles

        # Start each new alien at the mid top of screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the boss alien at its current location."""
        self.screen.blit(self.image, self.rect)

class Titan:
    """A class to manage the titan type alien."""

    def __init__(self, si_game):
        """Initialize the titan alien and set its starting position."""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        image_path = '/Users/ja1473/space-invaders/assets/images/titan.png'
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the titan alien at its current location."""
        self.screen.blit(self.image, self.rect)