class FleetCreationTest:
    def _create_fleet(self):
        """Create fleet of enemeies."""
        # Add aliens until there is no room left.
        # Space between aliens is one alien in width
        if self.boss_fight == False:
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size # Tuple containing width and height
        
            # Base number of alien spawns
            num_aliens = randint(3,8)

            # Spawn logic
            possible_x = [
                x for x in range(0, self.settings.screen_width - alien_width, alien_width * 2)
            ]

            # Shuffle and spawn
            spawn_xs = random.sample(possible_x, min(num_aliens, len(possible_x)))

            # Make our fleet
            for x in spawn_xs:
                self._create_alien(x, alien_height)