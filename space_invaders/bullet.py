import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): # Sprite lets you group related elements together
    """A class to manage ship projectiles."""

    def __init__(self, si_game):
        """Initialize projectile and starting position."""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        #Load projectile
        image_path = '/Users/ja1473/space-invaders/assets/images/test_bullet.png'
        #image_path = '/Users/ja1473/space-invaders/assets/images/ship_projectile.png'
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

        # Spawn bullet in front of ship
        self.rect.midtop = si_game.ship.rect.midtop

        # Store a float for the bullets exact position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw bullet to the screen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move bullet up."""
        # No need for complicated movement logic like the ship
        # As soon as the bullet spawns it will move which is what we want!
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y