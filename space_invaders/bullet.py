import pygame

class Bullet:
    """A class to manage ship projectiles."""

    def __init__(self, si_game):
        """Initialize projectile and starting position."""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.movement = False

        #Load projectile
        image_path = '/Users/ja1473/space-invaders/assets/images/ship_projectile.png'
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen_rect.bottomleft

    def blitme(self):
        """Draw bullet to the screen."""
        self.screen.blit(self.image, self.rect)

    def bullet_movement(self):
        """Initialize bullet movement."""

        if self.movement:
            self.rect.y -= 1