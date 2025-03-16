# MenuInterface.py
import pygame

# Function to render text on the screen
def render_text(screen, text, x, y, font, color):
    rendered_text = font.render(text, True, color)  # Text color dynamically passed
    screen.blit(rendered_text, (x, y))

# Function to draw the main menu options
def draw_main_menu(screen, font, mouse_pos):
    screen.fill((0, 0, 0))  # Black background

    # Menu options
    render_text(screen, "Main Menu", 140, 50, font, (255, 255, 255))  # White text for title

    # Define the colors for regular and hover states
    regular_color = (255, 255, 255)  # White
    hover_color = (255, 255, 0)  # Yellow for hover

    # Check if mouse is hovering over an option, change color accordingly
    option_1_color = hover_color if check_hover(mouse_pos, 100, 130, 140, 100) else regular_color
    option_2_color = hover_color if check_hover(mouse_pos, 100, 150, 140, 120) else regular_color
    option_3_color = hover_color if check_hover(mouse_pos, 100, 170, 140, 150) else regular_color
    exit_color = hover_color if check_hover(mouse_pos, 100, 250, 140, 220) else regular_color

    render_text(screen, "1. Tic-Tac-Toe", 140, 100, font, option_1_color)
    render_text(screen, "2. Trivia", 140, 150, font, option_2_color)
    render_text(screen, "3. TBD", 140, 200, font, option_3_color)
    render_text(screen, "4. Exit", 140, 250, font, exit_color)

    pygame.display.flip()  # Update the display to show the changes

# Check if mouse is hovering over a specific menu option
def check_hover(mouse_pos, x1, y1, x2, y2):
    mouse_x, mouse_y = mouse_pos
    return x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2
