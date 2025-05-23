"""Settings class for the space invaders game."""

class Settings:
    """Class to store all settings in Space Invaders."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200 # In pixels
        self.screen_height = 800 # In pixels
        self.bg_color = (40, 0, 80) # Lower the RBG values for darker colors
        self.ship_speed = 1.5 # Base ship speed
        self.bullet_speed = 10 # Base bullet speed
        self.alien_speed = 1 # Mob speed
        self.mushroom_speed = 1.5 # Second tier enemy speed
        self.boss_alien_speed = 2 # Boss speed
        self.titan_speed = 5 # Titan speed