# Breakout.py
import pygame

def breakout_screen(screen, font):
    screen.fill((0, 0, 0))  # Black background
    text = font.render("Breakout Screen", True, (255, 255, 255))  # White text
    screen.blit(text, (100, 100))  # Position text on the screen
    pygame.display.flip()  # Switches to the screen
