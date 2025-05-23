"""Settings class for the space invaders game."""

class Settings:
    """Class to store all settings in Space Invaders."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200 # In pixels
        self.screen_height = 800 # In pixels
        self.bg_color = (40, 0, 80) # Lower the RBG values for darker colors