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
        self.ship_speed = 1.5 # Base ship speed
        self.bullet_speed = 10 # Base bullet speed
        self.bullets_allowed = 5 # Max bullets allowed on screen
        self.bullet_damage = 2.5

        # Mob settings
        self.alien_speed = 1 # Mob speed
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right: -1 represents left
        self.fleet_direction = 1

        # Mushroom boss settings
        self.mushroom_speed = 1.5 # Second tier enemy speed

        # Antler boss settings
        self.boss_alien_speed = 2 # Boss speed

        # Titan settings
        self.titan_speed = 5 # Titan speed