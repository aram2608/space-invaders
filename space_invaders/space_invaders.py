import sys

import pygame

from space_invaders.settings import Settings
from space_invaders.ship import Ship
from space_invaders.bullet import Bullet
from space_invaders.alien import Alien, BossAlien, Titan, MushroomBoss

class SpaceInvaders:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() # initializes background settings pygame needs to work properly
        self.clock = pygame.time.Clock() # create Clock instance
        self.settings = Settings()

        # this makes the screen available to all methods in the class
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Space Invaders")

        # Initialize the character/object instances
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.alien = Alien(self)
        self.boss_alien = BossAlien(self)
        self.titan = Titan(self)
        self.mushroom_boss = MushroomBoss(self)

        # Set background color, RBG values are used
        self.bg_color = (63, 0, 70) # Lower RBG values for darker colors

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullet.bullet_movement()
            self._update_screen()
            # A frame rate of 60 fps
            self.clock.tick(60)

    # Helper methods use the following syntax _method_name, underscore goes first.
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            # Move ship up
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move ship down
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.bullet.movement = True

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            # Move ship up
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            # Move ship down
            self.ship.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
    # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.alien.blitme()
        self.bullet.blitme()
        self.boss_alien.blitme()
        self.titan.blitme()
        self.mushroom_boss.blitme()
    # Make the most recently drawn screen visible
        pygame.display.flip()