import pygame
import sys
import numpy
from TicTacToe import tic_tac_toe
from Trivia import trivia_game
from Breakout import main
import numpy as np
import webbrowser

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Load and play background music
# place it here

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
DARK_BLUE = (10, 25, 50)
LIGHT_BLUE = (50, 120, 200)
GRAY = (100, 100, 100)

# Font settings
font = pygame.font.Font(None, 40)

# Function to render text
def render_text(screen, text, x, y, font, color):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to check if mouse is hovering over text
def check_hover(mouse_pos, x, y, font, text):
    mouse_x, mouse_y = mouse_pos
    text_width, text_height = font.size(text)
    return x <= mouse_x <= x + text_width and y <= mouse_y <= y + text_height

# Function to draw background gradient
def draw_gradient_background(screen, width, height):
    for y in range(height):
        color = (DARK_BLUE[0] + y // 10, DARK_BLUE[1] + y // 5, DARK_BLUE[2] + y // 3)
        pygame.draw.line(screen, color, (0, y), (width, y))

# Function to handle menu navigation
def navigate(option):
    if option == 1:
        webbrowser.open(r"https://github.com/javonpayne100/CMSC495Capstone")
    elif option == 2:
        tic_tac_toe()
    elif option == 3:
        pygame.display.set_mode((600, 500))  # change this here to keep the game scrren trvia size.
        trivia_game()
    elif option == 4:
        pygame.display.set_mode((750, 450))  # change this here to keep the game scrren breakout.
        main()
    elif option == 5:
        pygame.mixer.music.stop()
        print("Exiting program...")
        pygame.quit()
        exit()

# Function to draw the main menu
def draw_main_menu(screen, font, mouse_pos):
    screen.fill(BLACK)  # Clear screen
    draw_gradient_background(screen, SCREEN_WIDTH, SCREEN_HEIGHT)  # Apply gradient

    # Menu title
    title_font = pygame.font.Font(None, 50)
    title_x = SCREEN_WIDTH // 2 - title_font.size("Main Menu")[0] // 2  # Centered title
    render_text(screen, "Main Menu", title_x, 50, title_font, WHITE)

    # Define menu options (positioned dynamically)
    options = [
        "1. Information",
        "2. Tic-Tac-Toe",
        "3. Trivia",
        "4. Breakout",
        "5. Exit"
    ]

    start_y = 130  # First option position
    spacing = 60  # Space between options

    for index, text in enumerate(options):
        x = SCREEN_WIDTH // 2 - font.size(text)[0] // 2  # Center text
        y = start_y + index * spacing

        hover = check_hover(mouse_pos, x, y, font, text)
        color = YELLOW if hover else WHITE

        # Rounded button effect
        text_width, text_height = font.size(text)
        pygame.draw.rect(screen, GRAY if hover else BLACK, (x - 10, y - 5, text_width + 20, text_height + 10), border_radius=10)
        pygame.draw.rect(screen, WHITE, (x - 10, y - 5, text_width + 20, text_height + 10), 2, border_radius=10)  # Border

        # Render text with hover effect (no glow now)
        render_text(screen, text, x, y, font, color)

    pygame.display.flip()  # Update the display

# Main loop
def main_menu():
    pygame.mixer.music.stop()
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        draw_main_menu(screen, font, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse click to navigate
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # Check which option was clicked
                for index, text in enumerate(["1. Information", "2. Tic-Tac-Toe", "3. Trivia", "4. TBD", "5. Exit"]):
                    x = SCREEN_WIDTH // 2 - font.size(text)[0] // 2
                    y = 130 + index * 60  # Match positions
                    if check_hover((mouse_x, mouse_y), x, y, font, text):
                        navigate(index + 1)  # Option starts from 1

# Start with the main menu
main_menu()

pygame.quit()