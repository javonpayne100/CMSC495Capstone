# MenuInterface.py
import pygame

def render_text_centered(screen, text, y, font, color, screen_width):
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=(screen_width // 2, y))
    screen.blit(rendered_text, text_rect)
    return text_rect  # return the clickable area

def draw_main_menu(screen, font, mouse_pos):
    screen.fill((0, 0, 0))
    screen_width = screen.get_width()

    regular_color = (255, 255, 255)
    hover_color = (255, 255, 0)

    option_rects = {}

    # Title
    render_text_centered(screen, "Main Menu", 80, font, (255, 255, 255), screen_width)

    # Menu Options
    options = {
        '1': "1. Tic-Tac-Toe",
        '2': "2. Trivia",
        '3': "3. Breakout",
        '4': "4. Exit"
    }

    y_positions = {
        '1': 140,
        '2': 190,
        '3': 240,
        '4': 290
    }

    for key in options:
        y = y_positions[key]
        text = options[key]
        is_hovered = False

        temp_rect = render_text_centered(screen, text, y, font, regular_color, screen_width)
        if temp_rect.collidepoint(mouse_pos):
            is_hovered = True

        color = hover_color if is_hovered else regular_color
        option_rects[key] = render_text_centered(screen, text, y, font, color, screen_width)

    pygame.display.flip()

    return option_rects  # return clickable areas
