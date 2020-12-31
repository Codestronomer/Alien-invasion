import sys

import pygame
from alien import Alien
import sky_function as sf

def blue_sky():
    """initializes pygame and the screen object """
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Blue Sky")
    bg_color = (230, 230, 23)

    alien = Alien(screen)
    # Start the main loop for the game
    while True:

        # Set background color for the game.
        screen.fill(bg_color)
        alien.blitme()
        sf.check_event(alien)
        alien.update()
        # Make the recent  screen drawn.
        pygame.display.flip()

blue_sky()