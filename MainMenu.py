# MainMenu.py
import pygame
import sys
from MenuInterface import draw_main_menu
from TicTacToe import tic_tac_toe_screen
from Trivia import trivia_screen
from TBD import tbd_screen

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Set up font
font = pygame.font.SysFont('Arial', 30)

# Coordinates for menu options (x1, x2, y1, y2 for each option)
MENU_OPTIONS = {
    '1': (100, 300, 130, 180),  # TicTacToe
    '2': (100, 300, 190, 240),  # Trivia
    '3': (100, 300, 250, 300),  # TBD
    '4': (100, 300, 310, 360)   # Exit (adjusted to give more space)
}

# Main game loop
def main():
    current_scene = 'menu'  # Start with the main menu
    mouse_pos = (0, 0)

    while True:
        # Draw the current scene (menu or options)
        if current_scene == 'menu':
            draw_main_menu(screen, font, mouse_pos)  # Draw the main menu screen
        elif current_scene == 'tic_tac_toe':
            tic_tac_toe_screen(screen, font)  # Draw TicTacToe screen
        elif current_scene == 'trivia':
            trivia_screen(screen, font)  # Draw Trivia screen
        elif current_scene == 'tbd':
            tbd_screen(screen, font)  # Draw TBD screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos  # Update mouse position on movement

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                print(f"Mouse clicked at: {mouse_x}, {mouse_y}")  # Debugging output

                # Check if the mouse click is within the bounds of an option
                if MENU_OPTIONS['1'][0] <= mouse_x <= MENU_OPTIONS['1'][1] and MENU_OPTIONS['1'][2] <= mouse_y <= MENU_OPTIONS['1'][3]:
                    print("TicTacToe clicked!")
                    current_scene = 'tic_tac_toe'  # Switch to TicTacToe screen
                elif MENU_OPTIONS['2'][0] <= mouse_x <= MENU_OPTIONS['2'][1] and MENU_OPTIONS['2'][2] <= mouse_y <= MENU_OPTIONS['2'][3]:
                    print("Trivia clicked!")
                    current_scene = 'trivia'  # Switch to Trivia screen
                elif MENU_OPTIONS['3'][0] <= mouse_x <= MENU_OPTIONS['3'][1] and MENU_OPTIONS['3'][2] <= mouse_y <= MENU_OPTIONS['3'][3]:
                    print("TBD clicked!")
                    current_scene = 'tbd'  # Switch to TBD screen
                elif MENU_OPTIONS['4'][0] <= mouse_x <= MENU_OPTIONS['4'][1] and MENU_OPTIONS['4'][2] <= mouse_y <= MENU_OPTIONS['4'][3]:
                    print("Exit clicked!")
                    pygame.quit()
                    sys.exit()

            # Check for 'Q' key press to return to the menu from options
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    current_scene = 'menu'

        pygame.time.Clock().tick(60)  # Frame rate (60 FPS)

if __name__ == "__main__":
    main()
