# MainMenu.py
import pygame
import sys
from MenuInterface import draw_main_menu
from TicTacToe import tic_tac_toe_screen
from Trivia import trivia_screen
from Breakout import breakout_screen  

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
    '1': (140, 300, 100, 140),  # TicTacToe
    '2': (140, 300, 150, 190),  # Trivia
    '3': (140, 300, 200, 240),  # Breakout (was TBD)
    '4': (140, 300, 250, 290)   # Exit
}

# Main game loop
def main():
    current_scene = 'menu'
    mouse_pos = (0, 0)

    while True:
        if current_scene == 'menu':
            draw_main_menu(screen, font, mouse_pos)
        elif current_scene == 'tic_tac_toe':
            tic_tac_toe_screen(screen, font)
        elif current_scene == 'trivia':
            trivia_screen(screen, font)
        elif current_scene == 'breakout':
            breakout_screen(screen, font)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if MENU_OPTIONS['1'][0] <= mouse_x <= MENU_OPTIONS['1'][1] and MENU_OPTIONS['1'][2] <= mouse_y <= MENU_OPTIONS['1'][3]:
                    current_scene = 'tic_tac_toe'
                elif MENU_OPTIONS['2'][0] <= mouse_x <= MENU_OPTIONS['2'][1] and MENU_OPTIONS['2'][2] <= mouse_y <= MENU_OPTIONS['2'][3]:
                    current_scene = 'trivia'
                elif MENU_OPTIONS['3'][0] <= mouse_x <= MENU_OPTIONS['3'][1] and MENU_OPTIONS['3'][2] <= mouse_y <= MENU_OPTIONS['3'][3]:
                    current_scene = 'breakout'  
                elif MENU_OPTIONS['4'][0] <= mouse_x <= MENU_OPTIONS['4'][1] and MENU_OPTIONS['4'][2] <= mouse_y <= MENU_OPTIONS['4'][3]:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    current_scene = 'menu'

        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
