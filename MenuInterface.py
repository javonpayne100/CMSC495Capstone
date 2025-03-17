# MenuInterface.py
import pygame

def render_text(screen, text, x, y, font, color):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def draw_main_menu(screen, font, mouse_pos):
    screen.fill((0, 0, 0))

    render_text(screen, "Main Menu", 140, 50, font, (255, 255, 255))

    regular_color = (255, 255, 255)
    hover_color = (255, 255, 0)

    option_1_color = hover_color if check_hover(mouse_pos, 140, 100, 300, 140) else regular_color
    option_2_color = hover_color if check_hover(mouse_pos, 140, 150, 300, 190) else regular_color
    option_3_color = hover_color if check_hover(mouse_pos, 140, 200, 300, 240) else regular_color
    exit_color = hover_color if check_hover(mouse_pos, 140, 250, 300, 290) else regular_color

    render_text(screen, "1. Tic-Tac-Toe", 140, 100, font, option_1_color)
    render_text(screen, "2. Trivia", 140, 150, font, option_2_color)
    render_text(screen, "3. Breakout", 140, 200, font, option_3_color)  
    render_text(screen, "4. Exit", 140, 250, font, exit_color)

    pygame.display.flip()

def check_hover(mouse_pos, x1, y1, x2, y2):
    mouse_x, mouse_y = mouse_pos
    return x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2
