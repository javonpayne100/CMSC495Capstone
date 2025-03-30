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
    screen.fill(BLACK)
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
            render_text("Enter Your Name:", SCREEN_WIDTH // 2 - 140, 100, font, YELLOW)
            pygame.draw.rect(screen, box_color, input_box, 2)
            text_surface = font.render(text, True, WHITE)
            screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
            pygame.display.flip()

    elif selected_mode == 2:
        # Two players mode
        screen.fill(BLACK)
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
            render_text("Enter Player 1 Name:", SCREEN_WIDTH // 2 - 150, 100, font, YELLOW)
            pygame.draw.rect(screen, WHITE, input_box_1, 2)
            text_surface_1 = font.render(text_1, True, WHITE)
            screen.blit(text_surface_1, (input_box_1.x + 10, input_box_1.y + 10))
            pygame.display.flip()

        # Now for Player 2
        screen.fill(BLACK)
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
    screen.fill(BLACK)
    render_text("Select a Category:", SCREEN_WIDTH // 2 - 140, 50, font, YELLOW)

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
    stop_trivia_music()  # Stop music after gameplay
    add_player_screen()  # Collect player names
    selected_category = select_category()  # Select a category
    question_pool = questions_data[selected_category]  # Use the full question pool

    if len(question_pool) < 5 * len(players):  # Ensure there are enough questions for all players
        screen.fill(BLACK)
        render_text("Not enough questions in this category!", 50, SCREEN_HEIGHT // 2, font, RED)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        return

    play_trivia_music()  # Start gameplay music
    scores = {}  # Dictionary to store each player's session score

    # Shuffle the entire question pool to ensure random questions
    random.shuffle(question_pool)

    for player in players:
        screen.fill(BLACK)
        render_text(f"{player}, press any key when ready!", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2, font, YELLOW)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False

        session_score = 0
        session_questions = random.sample(question_pool, 5)  # Pick 5 unique random questions for each player
        clock = pygame.time.Clock()

        for question_data in session_questions:
            current_question = question_data["question"]
            answers = question_data["answers"]
            correct_index = question_data["correct"]
            time_left = 10.0
            answered = False
            selected_answer_index = None  # Track the selected answer index

            while time_left > 0 and not answered:
                dt = clock.tick(60) / 1000.0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for index, answer in enumerate(answers):
                            x = 50
                            y = 150 + index * 50
                            text_width, text_height = question_font.size(f"{index + 1}. {answer}")
                            if x <= mouse_x <= x + text_width and y <= mouse_y <= y + text_height:
                                selected_answer_index = index
                                answered = True
                                if index == correct_index:
                                    session_score += 1
                                break  # Prevent multiple answers from being selected

                screen.fill(BLACK)
                draw_background_gradient()
                render_text(f"{player}'s Turn", SCREEN_WIDTH // 2 - 100, 20, font, YELLOW)
                render_text(current_question, 50, 100, question_font, WHITE)

                # Draw answers and highlight selected answers
                for index, answer in enumerate(answers):
                    answer_text = f"{index + 1}. {answer}"
                    if selected_answer_index is not None:
                        if index == correct_index:  # Correct answer
                            color = GREEN
                        elif index == selected_answer_index:  # Wrong answer selected by player
                            color = RED
                        else:
                            color = WHITE
                    else:
                        color = WHITE

                    render_text(answer_text, 50, 150 + index * 50, question_font, color)

                draw_timer((SCREEN_WIDTH - 60, SCREEN_HEIGHT - 60), 40, time_left, 10.0)
                render_text(f"Score: {session_score}", SCREEN_WIDTH - 200, 20, font, WHITE)
                pygame.display.flip()
                time_left -= dt

            # After the answer is selected, show the result for a brief moment
            if selected_answer_index is not None:
                time.sleep(1)  # Wait for 1 second to show the highlight before moving to the next question
            else:
                # If time runs out without an answer, highlight the correct one in green
                screen.fill(BLACK)
                draw_background_gradient()
                render_text(f"{player}'s Turn", SCREEN_WIDTH // 2 - 100, 20, font, YELLOW)
                render_text(current_question, 50, 100, question_font, WHITE)

                # Show the correct answer in green
                for index, answer in enumerate(answers):
                    color = GREEN if index == correct_index else WHITE
                    render_text(f"{index + 1}. {answer}", 50, 150 + index * 50, question_font, color)

                draw_timer((SCREEN_WIDTH - 60, SCREEN_HEIGHT - 60), 40, time_left, 10.0)
                render_text(f"Score: {session_score}", SCREEN_WIDTH - 200, 20, font, WHITE)
                pygame.display.flip()
                time.sleep(1)

        scores[player] = session_score
        time.sleep(1)

    stop_trivia_music()  # Stop music after gameplay

    # Final results screen
    screen.fill(BLACK)
    render_text("Final Results", SCREEN_WIDTH // 2 - 100, 50, font, YELLOW)
    y_offset = 100
    for player in players:
        render_text(f"{player}: {scores[player]}", SCREEN_WIDTH // 2 - 100, y_offset, font, WHITE)
        y_offset += 50

    # Determine the winner
    winners = [player for player, score in scores.items() if score == max(scores.values())]
    render_text(f"{winners[0]} wins!", SCREEN_WIDTH // 2 - 100, y_offset + 50, font, YELLOW)
    pygame.display.flip()
    time.sleep(3)

    pygame.quit()


# ----------------------------
# Main Guard
# ----------------------------
if __name__ == "__main__":
    trivia_game()
