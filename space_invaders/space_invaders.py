import sys
from random import randint
from time import sleep

import pygame

from space_invaders.settings import Settings
from space_invaders.ship import Ship
from space_invaders.bullet import Bullet
from space_invaders.alien import Alien, BossAlien, Titan, MushroomBoss
from space_invaders.game_stats import GameStats, GameOver
from space_invaders.buttons import Button

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

        # Create an instance to store game statisitcs
        self.stats = GameStats(self)

        # Initialize the character/object instances
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Initialize enemy types
        self.aliens = pygame.sprite.Group()
        self.boss_alien = pygame.sprite.Group()
        self.titan = pygame.sprite.Group()
        self.mushroom_boss = pygame.sprite.Group()

        # Game over screen
        self.game_over_text = GameOver(self)

        # Spawn logic
        self._create_fleet()
        self._spawn_boss()

        # Set background color, RBG values are used
        self.bg_color = (63, 0, 70) # Lower RBG values for darker colors

        # Start the game in an active state
        self.game_active = False

        # Game over state
        self.game_end = False

        # Make the play button
        self.play_button = Button(self, "Play")
        self.retry_button = Button(self, "R to try again")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            # Components that should only be active while game is active.
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_mobs()

            # Redraw screen
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

    def _check_retry(self):
        """Start a new game after a game over."""
        self.game_end = False
        self.game_active = True
        self.stats.ships_left += 3

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # Clear background
        self.screen.fill(self.settings.bg_color)

        if self.game_end:
            self.game_over_text.blitme()
            self.retry_button.draw_button()

        elif not self.game_active:
            # Game is idle
            self.play_button.draw_button()

        else:
            # Active game running
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.blitme()

            self.aliens.draw(self.screen)
            self.boss_alien.draw(self.screen)
            self.mushroom_boss.draw(self.screen)
            self.titan.draw(self.screen)

        # Flip everything to the screen
        pygame.display.flip()

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
        elif event.key == pygame.K_r and self.stats.ships_left == 0:
            self._check_retry()
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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullets and aliens that have collided."""
        # Remove bullets and aliens that have collieded.
        collisions = pygame.sprite.groupcollide( # groupcollide() compares two groups rects and sees if they hit each other
            self.bullets, self.aliens, False, True # it then stores the two objects in a dictionary.
        ) # The two true arguments tell pygame to remove the objects that are hit.

        # Logic for spawning more mobs
        if not self.aliens: # Check to see if alien group is empty
            #Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """Respond to ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrease the number of ships left.
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and allines
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_end = True

    def _create_fleet(self):
        """Create fleet of enemeies."""
        # Add aliens until there is no room left.
        # Space between aliens is one alien in width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size # Tuple containing width and height
        
        # We get the base dimensions
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

    def _update_mobs(self):
        """Update mob alien position."""
        self._check_fleet_edges()
        self.aliens.update()

        # Detect alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this as if the ship got hit.
                self._ship_hit()
                break # No reason to check every alien, just the first that reaches bottom

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's directions."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _spawn_boss(self):
        """A manager for the boss classes."""
        boss_spawn_chance = randint(1,100)
        titan = Titan(self)
        mushroom = MushroomBoss(self)
        boss_alien = BossAlien(self)