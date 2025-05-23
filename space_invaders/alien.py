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

        # Position handling
        if position == "topleft":
            self.rect.topleft = self.screen_rect.topleft
        elif position == "topright":
            self.rect.topright = self.screen_rect.topright
        elif position == "midtop":
            self.rect.midtop = self.screen_rect.midtop
        elif position == "midleft":
            self.rect.midleft = self.screen_rect.midleft
        elif position == "midright":
            self.rect.midright = self.screen_rect.midright
        elif position == "center":
            self.rect.center = self.screen_rect.center
        elif position == "random":
            # Spawn anywhere across the top row
            max_x = self.screen_rect.width - self.rect.width # Differnece between screen and alien
            random_x = randint(0, max_x) # randomizer
            self.rect.x = random_x # Sets the x position randomly
            self.rect.y = 0  # Top of screen


    def blitme(self):
        """Draws the enemey to the screen."""
        self.screen.blit(self.image, self.rect)

class Alien(EnemyRender):
    """Base mob type alien."""
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/alien.png', position='random')
        self.health = 10

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
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/mushroom_boss.png', position='radnom')
        self.health = 25
