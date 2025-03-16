# TicTacToe.py
import pygame

def tic_tac_toe_screen(screen, font):
    # Display TicTacToe content here
    screen.fill((0, 0, 0))  # Black background
    text = font.render("Tic Tac Toe Game", True, (255, 255, 255))  # White text
    screen.blit(text, (100, 100))  # Position the text on the screen
    pygame.display.flip()  # Switches to the screen
