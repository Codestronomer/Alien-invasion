import sys

import pygame

def checks_key_down_events(alien, event):
    """Responds to key presses."""
    if event.key == pygame.KEYUP:
        alien.moving_up = True
    elif event.key == pygame.KEYDOWN:
        alien.moving_down = True
    elif event.key == pygame.K_LEFT:
        alien.moving_left = True
    elif event.key == pygame.K_RIGHT:
        alien.moving_right = True

def checks_key_up_events(alien, event):
    """Responds to key releases."""
    if event.key == pygame.K_UP:
        alien.moving_up = False
    elif event.key == pygame.K_DOWN:
        alien.moving_down = False
    elif event.key == pygame.K_LEFT:
        alien.moving_left = False
    elif event.key == pygame.K_RIGHT:
        alien.moving_right = False

def check_event(alien):
    """Responds to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checks_key_down_events(alien, event)
        elif event.type == pygame.KEYUP:
            checks_key_up_events(alien, event)