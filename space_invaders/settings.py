"""Settings class for the space invaders game."""

class Settings:
    """Class to store all settings in Space Invaders."""

    def __init__(self):
        """Initialize the game's settings."""
        # Base game settings
        self.screen_width = 1200 # In pixels
        self.screen_height = 800 # In pixels
        self.bg_color = (40, 0, 80) # Lower the RBG values for darker colors

        # Ship settings
        self.ship_limit = 3 # Number of lives

        # Bullet Settings
        self.bullets_allowed = 5 # Max bullets allowed on screen

        # Mob settings
        self.fleet_drop_speed = 10
        self.alien_kills = 0

        # Mushroom boss settings
        self.mushroom_speed = 1.5 # Second tier enemy speed
        self.mushroom_health = 5

        # Antler boss settings
        self.boss_alien_speed = 2 # Boss speed
        self.boss_alien_health = 10

        # Titan settings
        self.titan_speed = 5 # Titan speed
        self.titan_health = 25

        # Game speed up
        self.speedup_scale = 1.1 # How quickly the game speeds up
        self.score_scale = 1.5 # How quickly point values increase
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that can change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.mob_points = 50

        # Fleet direction of 1 represents right: -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.mob_points = int(self.mob_points * self.score_scale)