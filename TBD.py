# TBD.py
import pygame

def tbd_screen(screen, font):
    screen.fill((0, 0, 0))  # Black background
    text = font.render("TBD Screen", True, (255, 255, 255))  # White text
    screen.blit(text, (100, 100))  # Position text on the screen
    pygame.display.flip()  # Switches to the screen
