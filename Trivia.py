import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trivia Game")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (30, 30, 60)
LIGHT_BLUE = (50, 50, 150)

# Font settings
font = pygame.font.Font(None, 40)
question_font = pygame.font.Font(None, 30)

# List of trivia questions with multiple answers
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct": 2  # Correct answer is "Paris"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "answers": ["Shakespeare", "Dickens", "Austen", "Tolkien"],
        "correct": 0  # Correct answer is "Shakespeare"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct": 2  # Correct answer is "Jupiter"
    },
]

random.shuffle(questions)  # Shuffle questions for variety


# Function to render text
def render_text(text, x, y, font, color):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))


# Function to draw donut-shaped countdown timer
def draw_timer(center, radius, time_left, max_time):
    color = GREEN if time_left > 6 else YELLOW if time_left > 3 else RED
    pygame.draw.circle(screen, GRAY, center, radius)  # Outer circle background
    pygame.draw.circle(screen, BLACK, center, radius - 10)  # Inner cutout

    angle_start = -90
    angle_end = angle_start + (time_left / max_time) * 360
    step = 3  # Smoother effect
    for i in range(int(angle_start), int(angle_end), step):
        radian = math.radians(i)
        x = center[0] + int(radius * math.cos(radian))
        y = center[1] + int(radius * math.sin(radian))
        pygame.draw.circle(screen, color, (x, y), 4)

    # Draw central text
    timer_text = font.render(str(time_left), True, WHITE)
    screen.blit(timer_text, (center[0] - 10, center[1] - 10))


# Function to draw the question and answers
def draw_trivia_screen(question_data, score, time_left):
    # Gradient background
    for i in range(SCREEN_HEIGHT):
        color_gradient = (
            DARK_BLUE[0] + (LIGHT_BLUE[0] - DARK_BLUE[0]) * i // SCREEN_HEIGHT,
            DARK_BLUE[1] + (LIGHT_BLUE[1] - DARK_BLUE[1]) * i // SCREEN_HEIGHT,
            DARK_BLUE[2] + (LIGHT_BLUE[2] - DARK_BLUE[2]) * i // SCREEN_HEIGHT,
        )
        pygame.draw.line(screen, color_gradient, (0, i), (SCREEN_WIDTH, i))

    # Display question
    render_text(question_data["question"], 50, 50, question_font, WHITE)

    # Display answers as buttons
    start_y = 150
    for index, answer in enumerate(question_data["answers"]):
        answer_text = f"{index + 1}. {answer}"
        render_text(answer_text, 50, start_y + index * 60, font, WHITE)

    # Display score
    render_text(f"Score: {score}", SCREEN_WIDTH - 150, 10, font, YELLOW)

    # Draw countdown timer at bottom right
    draw_timer((SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50), 40, time_left, 10)

    pygame.display.flip()  # Update the display


# Function to check if the user clicked on a specific answer
def check_answer(mouse_pos, question_data):
    mouse_x, mouse_y = mouse_pos
    start_y = 150

    # Check for each answer button
    for index, answer in enumerate(question_data["answers"]):
        answer_width, answer_height = font.size(f"{index + 1}. {answer}")
        x = 50
        y = start_y + index * 60
        if x <= mouse_x <= x + answer_width and y <= mouse_y <= y + answer_height:
            return index
    return None


# Function to display play again screen
def play_again_screen(score):
    screen.fill(BLACK)
    render_text(f"Game Over! Final Score: {score}", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, font, YELLOW)
    render_text("Play again? (Y/N)", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, font, WHITE)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting = False
                    trivia_game()
                elif event.key == pygame.K_n:
                    pygame.quit()
                    exit()


# Main Trivia Game Function
def trivia_game():
    running = True
    score = 0
    question_index = 0
    timer_start = pygame.time.get_ticks()
    time_limit = 10  # 10 seconds per question

    while running:
        current_time = pygame.time.get_ticks()
        time_left = max(0, time_limit - (current_time - timer_start) // 1000)
        current_question = questions[question_index]
        draw_trivia_screen(current_question, score, time_left)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_answer = check_answer(mouse_pos, current_question)
                if selected_answer is not None:
                    if selected_answer == current_question["correct"]:
                        score += 1
                    question_index += 1
                    timer_start = pygame.time.get_ticks()
                    if question_index >= len(questions):
                        running = False

        if time_left == 0:
            question_index += 1
            timer_start = pygame.time.get_ticks()
            if question_index >= len(questions):
                running = False

        pygame.display.flip()

    play_again_screen(score)


# Start the game
trivia_game()
