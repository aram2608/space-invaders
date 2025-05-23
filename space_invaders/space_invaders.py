import sys
from random import randint

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
            (0,0), pygame.FULLSCREEN
        )
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width

        pygame.display.set_caption("Space Invaders")

        # Initialize the character/object instances
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Initialize enemy types
        self.aliens = pygame.sprite.Group()
        self.boss_alien = pygame.sprite.Group()
        self.titan = pygame.sprite.Group()
        self.mushroom_boss = pygame.sprite.Group()

        # Spawn logic
        self.__create_fleet()
        self._spawn_boss()

        # Set background color, RBG values are used
        self.bg_color = (63, 0, 70) # Lower RBG values for darker colors

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
            self._fire_bullet()
        elif event.key == pygame.K_q: # Shortcut to quit game 'q'
            sys.exit()

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

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Manages fired bullets."""
        # Update bullet postions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
             # Kill if it moves off-screen
            if bullet.rect.bottom <+ 0:
                bullet.kill()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        #Character specific items
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.blitme()

        # Draw in enemy classes
        self.aliens.draw(self.screen)
        self.boss_alien.draw(self.screen)
        self.mushroom_boss.draw(self.screen)
        self.titan.draw(self.screen)
        
    # Make the most recently drawn screen visible
        pygame.display.flip()

    def __create_fleet(self):
        """Create fleet of enemeies."""
        # Add aliens until there is no room left.
        # Space between aliens is one alien in width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size # Tuple containing width and height
        
        # we get the base dimensions
        current_x, current_y = alien_width, alien_height

        # Spawn logic
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row, reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Method to spawn aliens."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _spawn_boss(self):
        """A manager for the boss classes."""
        boss_spawn_chance = randint(1,100)
        titan = Titan(self)
        mushroom = MushroomBoss(self)
        boss_alien = BossAlien(self)