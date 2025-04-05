import pygame
import random
import math
import time
import json

# ----------------------------
# Initialization
# ----------------------------
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trivia Game")

# Colors and Fonts
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (30, 30, 60)
LIGHT_BLUE = (50, 50, 150)
BUTTON_COLOR = (100, 200, 150) # color for button

font = pygame.font.Font(None, 40)
question_font = pygame.font.Font(None, 30)


# ----------------------------
# Load Questions from JSON
# ----------------------------
def load_questions():
    try:
        with open("questions.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: questions.json file not found.")
        pygame.quit()
        exit()
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from questions.json.")
        pygame.quit()
        exit()


questions_data = load_questions()


# ----------------------------
# Utility Functions
# ----------------------------
def play_trivia_music():
    pygame.mixer.music.load("Jeopardy_Music.wav")
    pygame.mixer.music.play(-1)


def stop_trivia_music():
    pygame.mixer.music.stop()


def render_text(text, x, y, font, color):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))


def draw_background_gradient():
    for i in range(SCREEN_HEIGHT):
        color_gradient = (
            DARK_BLUE[0] + (LIGHT_BLUE[0] - DARK_BLUE[0]) * i // SCREEN_HEIGHT,
            DARK_BLUE[1] + (LIGHT_BLUE[1] - DARK_BLUE[1]) * i // SCREEN_HEIGHT,
            DARK_BLUE[2] + (LIGHT_BLUE[2] - DARK_BLUE[2]) * i // SCREEN_HEIGHT,
        )
        pygame.draw.line(screen, color_gradient, (0, i), (SCREEN_WIDTH, i))


def draw_timer(center, radius, time_left, max_time):
    color = GREEN if time_left > 6 else YELLOW if time_left > 3 else RED
    pygame.draw.circle(screen, GRAY, center, radius)
    pygame.draw.circle(screen, BLACK, center, radius - 10)
    angle_start = -90
    angle_end = angle_start + (time_left / max_time) * 360
    pygame.draw.arc(screen, color, (center[0] - radius, center[1] - radius, 2 * radius, 2 * radius),
                    math.radians(angle_start), math.radians(angle_end), 10)
    timer_text = font.render(str(int(time_left)), True, WHITE)
    screen.blit(timer_text, (center[0] - 10, center[1] - 10))


# ----------------------------
# Menu Screens
# ----------------------------
def add_player_screen():
    global players
    players = []

    # Select the number of players
    screen.fill(BLACK)  # You can change this to a custom color, if needed

    # Draw the gradient background (same as in trivia question screen)
    draw_background_gradient()

    render_text("Select the number of players:", SCREEN_WIDTH // 2 - 150, 50, font, YELLOW)
    render_text("1. One Player", SCREEN_WIDTH // 2 - 100, 150, font, WHITE)
    render_text("2. Two Players", SCREEN_WIDTH // 2 - 100, 200, font, WHITE)
    pygame.display.flip()

    selected_mode = None
    while selected_mode is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if SCREEN_WIDTH // 2 - 100 <= mouse_x <= SCREEN_WIDTH // 2 + 100:
                    if 150 <= mouse_y <= 200:  # One Player selected
                        selected_mode = 1
                    elif 200 <= mouse_y <= 250:  # Two Players selected
                        selected_mode = 2

    if selected_mode == 1:
        # Single player mode
        screen.fill(BLACK)
        draw_background_gradient()  # Use gradient background
        render_text("Enter Your Name:", SCREEN_WIDTH // 2 - 140, 100, font, YELLOW)
        pygame.display.flip()

        input_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, 200, 300, 50)
        active_box = True
        text = ""
        box_color = WHITE

        while active_box:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and text:
                        players = [text]  # Set the player's name
                        active_box = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

            screen.fill(BLACK)
            draw_background_gradient()  # Use gradient background
            render_text("Enter Your Name:", SCREEN_WIDTH // 2 - 140, 100, font, YELLOW)
            pygame.draw.rect(screen, box_color, input_box, 2)
            text_surface = font.render(text, True, WHITE)
            screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
            pygame.display.flip()

    elif selected_mode == 2:
        # Two players mode
        screen.fill(BLACK)
        draw_background_gradient()  # Use gradient background
        render_text("Enter Player 1 Name:", SCREEN_WIDTH // 2 - 150, 100, font, YELLOW)
        pygame.display.flip()

        input_box_1 = pygame.Rect(SCREEN_WIDTH // 2 - 150, 200, 300, 50)
        text_1 = ""
        active_box_1 = True
        while active_box_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and text_1:
                        players.append(text_1)  # Set Player 1's name
                        active_box_1 = False
                    elif event.key == pygame.K_BACKSPACE:
                        text_1 = text_1[:-1]
                    else:
                        text_1 += event.unicode

            screen.fill(BLACK)
            draw_background_gradient()  # Use gradient background
            render_text("Enter Player 1 Name:", SCREEN_WIDTH // 2 - 150, 100, font, YELLOW)
            pygame.draw.rect(screen, WHITE, input_box_1, 2)
            text_surface_1 = font.render(text_1, True, WHITE)
            screen.blit(text_surface_1, (input_box_1.x + 10, input_box_1.y + 10))
            pygame.display.flip()

        # Now for Player 2
        screen.fill(BLACK)
        draw_background_gradient()  # Use gradient background
        render_text("Enter Player 2 Name:", SCREEN_WIDTH // 2 - 150, 100, font, YELLOW)
        pygame.display.flip()

        input_box_2 = pygame.Rect(SCREEN_WIDTH // 2 - 150, 200, 300, 50)
        text_2 = ""
        active_box_2 = True
        while active_box_2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and text_2:
                        players.append(text_2)  # Set Player 2's name
                        active_box_2 = False
                    elif event.key == pygame.K_BACKSPACE:
                        text_2 = text_2[:-1]
                    else:
                        text_2 += event.unicode

            screen.fill(BLACK)
            draw_background_gradient()  # Use gradient background
            render_text("Enter Player 2 Name:", SCREEN_WIDTH // 2 - 150, 100, font, YELLOW)
            pygame.draw.rect(screen, WHITE, input_box_2, 2)
            text_surface_2 = font.render(text_2, True, WHITE)
            screen.blit(text_surface_2, (input_box_2.x + 10, input_box_2.y + 10))
            pygame.display.flip()

    pygame.display.flip()

# ----------------------------
# Category Selection Function
# ----------------------------
def select_category():
    categories = ["Science", "Math", "History", "Geography", "Literature"]

    # Fill the screen with the gradient background
    screen.fill(BLACK)
    draw_background_gradient()  # Call the gradient function to create the background

    render_text("Select a Category:", SCREEN_WIDTH // 2 - 140, 50, font, YELLOW)

    # Render the categories
    for index, category in enumerate(categories):
        render_text(f"{index + 1}. {category}", SCREEN_WIDTH // 2 - 100, 150 + (index * 50), font, WHITE)

    pygame.display.flip()

    selected_category = None
    while selected_category is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for index, category in enumerate(categories):
                    if SCREEN_WIDTH // 2 - 100 <= mouse_x <= SCREEN_WIDTH // 2 + 100:
                        if 150 + (index * 50) <= mouse_y <= 200 + (index * 50):  # Category selected
                            selected_category = category
                            break

    return selected_category


# ----------------------------
# Main Game Function
# ----------------------------
def trivia_game():
    while True:
        stop_trivia_music()
        global players
        players = []
        add_player_screen()
        selected_category = select_category()
        question_pool = questions_data[selected_category]

        if len(question_pool) < 5 * len(players):
            screen.fill(BLACK)
            render_text("Not enough questions in this category!", 50, SCREEN_HEIGHT // 2, font, RED)
            pygame.display.flip()
            time.sleep(3)
            return "menu"

        play_trivia_music()
        scores = {}
        random.shuffle(question_pool)

        for player in players:
            session_score = 0
            questions = random.sample(question_pool, 5)
            clock = pygame.time.Clock()

            for q in questions:
                current_question = q["question"]
                answers = q["answers"]
                correct_index = q["correct"]
                time_left = 10.0
                answered = False
                selected_index = None

                while time_left > 0 and not answered:
                    dt = clock.tick(60) / 1000.0
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return "quit"
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mx, my = pygame.mouse.get_pos()
                            for i, a in enumerate(answers):
                                x, y = 50, 150 + i * 50
                                w, h = question_font.size(f"{i + 1}. {a}")
                                if x <= mx <= x + w and y <= my <= y + h:
                                    selected_index = i
                                    answered = True
                                    if i == correct_index:
                                        session_score += 1

                    screen.fill(BLACK)
                    draw_background_gradient()
                    render_text(f"{player}'s Turn", SCREEN_WIDTH // 2 - 100, 20, font, YELLOW)
                    render_text(current_question, 50, 100, question_font, WHITE)

                    for i, a in enumerate(answers):
                        color = (
                            GREEN if i == correct_index else
                            RED if i == selected_index else
                            WHITE
                        ) if selected_index is not None else WHITE
                        render_text(f"{i + 1}. {a}", 50, 150 + i * 50, question_font, color)

                    draw_timer((SCREEN_WIDTH - 60, SCREEN_HEIGHT - 60), 40, time_left, 10.0)
                    render_text(f"Score: {session_score}", SCREEN_WIDTH - 200, 20, font, WHITE)
                    pygame.display.flip()
                    time_left -= dt

                if selected_index is None:
                    time.sleep(1)

            scores[player] = session_score
            time.sleep(1)
##################################################################################################
# shows final results and player choice
        stop_trivia_music()
        result = show_final_results(scores)

        if result == "restart":
            continue
        elif result == "menu":
            return "menu"
        elif result == "quit":
            pygame.quit()
            exit()

def show_final_results(scores):
    """
    Displays final result screen after game ends
    Shows scores for players
    Provides buttons to play agains or return to menu
    """
    result = None
    button_font = pygame.font.Font(None, 36)
    #define button areas
    play_again_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 220, 200, 50)
    menu_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 290, 200, 50)
    quit_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 360, 200, 50)

    # Determine winner(s)
    highest_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == highest_score]

    while result is None:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(BLACK)
        draw_background_gradient()
        render_text("Final Results", SCREEN_WIDTH // 2 - 100, 40, font, YELLOW)
        # score display
        y_offset = 100
        for player in scores:
            render_text(f"{player}: {scores[player]}", SCREEN_WIDTH // 2 - 100, y_offset, font, WHITE)
            y_offset += 40

        # Show winner or tie
        if len(winners) == 1:
            render_text(f"{winners[0]} wins!", SCREEN_WIDTH // 2 - 100, y_offset + 10, font, GREEN)
        else:
            render_text("It's a Tie!", SCREEN_WIDTH // 2 - 100, y_offset + 10, font, GREEN)

        # Button hover colors
        play_color = (80, 220, 170) if play_again_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        menu_color = (80, 140, 220) if menu_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        quit_color = (200, 50, 50) if quit_rect.collidepoint(mouse_pos) else BUTTON_COLOR

        # Draw buttons
        pygame.draw.rect(screen, play_color, play_again_rect, border_radius=10)
        pygame.draw.rect(screen, menu_color, menu_rect, border_radius=10)
        pygame.draw.rect(screen, quit_color, quit_rect, border_radius=10)

        # Button text
        screen.blit(button_font.render("Play Again", True, WHITE), play_again_rect.move(35, 10))
        screen.blit(button_font.render("Main Menu", True, WHITE), menu_rect.move(30, 10))
        screen.blit(button_font.render("Quit", True, WHITE), quit_rect.move(75, 10))

        pygame.display.flip()
# event handler for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                result = "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(mouse_pos):
                    result = "restart"
                elif menu_rect.collidepoint(mouse_pos):
                    result = "menu"
                elif quit_rect.collidepoint(mouse_pos):
                    result = "quit"

    return result
# ----------------------------
# Main Guard
# ----------------------------
if __name__ == "__main__":
    trivia_game()
