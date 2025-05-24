import pygame
from pygame.sprite import Sprite
from random import randint

class EnemyRender(Sprite):
    """Base class for all enemies."""
    def __init__(self, si_game, image_path, position="random"): # self refernce for class and reference to SpaceInvaders instance
        """Initialize Sprite methods and enemy base attributes."""
        super().__init__()
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = si_game.settings

        # Load image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

       # Random spawn logic
        if position == "random":
            # Spawn anywhere across the top row
            max_x = self.screen_rect.width - self.rect.width # Difference between screen and alien
            random_x = randint(0, max_x) # randomizer
            self.rect.x = random_x # Sets the x position randomly
            self.rect.y = 0  # Top of screen


    def blitme(self):
        """Draws the enemy to the screen."""
        self.screen.blit(self.image, self.rect)

class Alien(EnemyRender):
    """Class for managing mod alien types."""
    def __init__(self, si_game):
        """Initialize Mob specific behavior."""
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/alien.png', position="None")

    def update(self):
        """Move the alien left or right."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at screen edge."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False

class BossAlien(EnemyRender):
    """Boss alien subtype."""
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/boss_alien.png', position='random')
        self.health = 25

class Titan(EnemyRender):
    """Titan class alien, most difficult boss in the game."""
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/titan.png', position='random')
        self.health = 100

class MushroomBoss(EnemyRender):
    """Special boss type alien."""
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/mushroom_boss.png', position='random')
        self.health = 10
