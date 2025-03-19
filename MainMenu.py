import pygame
import sys
from MenuInterface import draw_main_menu
from TicTacToe import tic_tac_toe_screen
from Trivia import trivia_screen
from Breakout import breakout_screen  

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")
font = pygame.font.SysFont('Arial', 30)

# Load background image
background_image = pygame.image.load("stars.png")  

# Initialize the sound system
pygame.mixer.init()

# Load sound files
wall_sound = pygame.mixer.Sound("wall.wav")
paddle_sound = pygame.mixer.Sound("paddle.wav")
brick_sound = pygame.mixer.Sound("brick.wav")
losing_sound = pygame.mixer.Sound("mixkit-player-losing-or-failing-2042.wav")  

# Load and play background music for the menu
pygame.mixer.music.load("C:/Users/todas/Downloads/CMSC495Capstone-main/mixkit-game-level-music-689.wav") 
pygame.mixer.music.play(-1, 0.0)  # Play the music indefinitely from the beginning

def main():
    current_scene = 'menu'
    mouse_pos = (0, 0)
    option_rects = {}  # Store clickable areas here

    while True:
        # Fill the screen with the background image before any other content
        screen.blit(background_image, (0, 0))  # Position the image at the top-left corner

        if current_scene == 'menu':
            option_rects = draw_main_menu(screen, font, mouse_pos)

        elif current_scene == 'tic_tac_toe':
            pygame.mixer.music.stop()  # Stop music when leaving the menu screen
            result = tic_tac_toe_screen(screen, font)
            if result == 'exit':  
                pygame.quit()
                sys.exit()
            elif result == 'menu':
                current_scene = 'menu'
                pygame.mixer.music.play(-1, 0.0)  # Restart music when back to the menu

        elif current_scene == 'trivia':
            pygame.mixer.music.stop()  # Stop music when leaving the menu screen
            result = trivia_screen(screen, font)
            if result == 'exit':
                pygame.quit()
                sys.exit()
            elif result == 'menu':
                current_scene = 'menu'
                pygame.mixer.music.play(-1, 0.0)  # Restart music when back to the menu

        elif current_scene == 'breakout':
            pygame.mixer.music.stop()  # Stop music when leaving the menu screen
            result = breakout_screen(screen, font, wall_sound, paddle_sound, brick_sound, losing_sound)  # Pass the losing_sound here
            if result == 'exit':
                pygame.quit()
                sys.exit()
            elif result == 'menu':
                current_scene = 'menu'
                pygame.mixer.music.play(-1, 0.0)  # Restart music when back to the menu

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_scene == 'menu' and option_rects:
                    for key, rect in option_rects.items():
                        if rect.collidepoint(event.pos):
                            if key == '1':
                                current_scene = 'tic_tac_toe'
                            elif key == '2':
                                current_scene = 'trivia'
                            elif key == '3':
                                current_scene = 'breakout'
                            elif key == '4':
                                pygame.quit()
                                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
