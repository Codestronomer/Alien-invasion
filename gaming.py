import pygame

from settings import Settings
from ship import Ship
import game_functions as game_func
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store the game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens.
    game_func.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:

        # Watch for mouse and keyboard events.
        game_func.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            game_func.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            game_func.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Redraw the screen during each pass through the loop.
        game_func.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()