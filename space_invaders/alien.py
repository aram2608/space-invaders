import pygame
from random import randint

class EnemyRender(pygame.sprite.Sprite):
    """Base class for all enemies."""
    def __init__(self, si_game, image_path, position="random"):
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
            spawn = randint(1, 3)
            if spawn == 1:
                self.rect.topleft = self.screen_rect.topleft
            elif spawn == 2:
                self.rect.topright = self.screen_rect.topright
            else:
                self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien(EnemyRender):
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/alien.png', position='random')

class BossAlien(EnemyRender):
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/boss_alien.png', position='random')

class Titan(EnemyRender):
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/titan.png', position='random')

class MushroomBoss(EnemyRender):
    def __init__(self, si_game):
        super().__init__(si_game, '/Users/ja1473/space-invaders/assets/images/mushroom_boss.png', position='radnom')
