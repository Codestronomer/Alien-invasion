import pygame
from pygame.sprite import Sprite

class   Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initializes the alien and its starting point"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loads the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new screen at the center of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact location
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if the alien touches the egde of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the screen at its current location"""
        self.screen.blit(self.image, self.rect)