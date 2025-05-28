import pygame.font
from pygame.sprite import Group
from space_invaders.lives import Lives

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, si_game):
        """Initialize scorekeeping attributes."""
        self.si_game = si_game
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.settings = si_game.settings
        self.stats = si_game.stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Number of lives remaining
        self.prep_lives()

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1) # rouns to the nearest 10
        score_str = f"{rounded_score:,}" # :, tells python to place commas where appropriate
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Store a highscore value."""
        high_score = round(self.stats.score, -1)
        high_score_str = f"High Score: {high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lives.draw(self.screen)

    def check_high_score(self):
        """Check to see if there are new high scores."""
        if self.stats.score > self.stats.score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_lives(self):
        """Show how many ships are left."""
        self.lives = Group()
        for life_number in range(self.stats.ships_left):
            life = Lives(self.si_game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 920
            self.lives.add(life)