import pygame
import random

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

# Function to render text
def render_text(text, x, y, font, color):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to draw the question and answers
def draw_trivia_screen(question_data, score):
    screen.fill(BLACK)  # Clear screen

    # Display question
    render_text(question_data["question"], 50, 50, question_font, WHITE)

    # Display answers as buttons
    start_y = 150
    for index, answer in enumerate(question_data["answers"]):
        answer_text = f"{index + 1}. {answer}"
        render_text(answer_text, 50, start_y + index * 60, font, WHITE)

    # Display score
    render_text(f"Score: {score}", SCREEN_WIDTH - 150, 10, font, YELLOW)

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

# Main Trivia Game Function
def trivia_game():
    running = True
    score = 0
    question_index = 0

    while running:
        current_question = questions[question_index]
        draw_trivia_screen(current_question, score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_answer = check_answer(mouse_pos, current_question)

                if selected_answer is not None:
                    if selected_answer == current_question["correct"]:
                        score += 1  # Correct answer
                    question_index += 1  # Move to the next question

                    # If all questions are answered, show final score
                    if question_index >= len(questions):
                        running = False

        pygame.display.flip()

    # End Screen (show final score)
    screen.fill(BLACK)
    render_text(f"Game Over! Final Score: {score}", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, font, YELLOW)
    pygame.display.flip()

    pygame.time.wait(3000)  # Wait 3 seconds before closing
    pygame.quit()
