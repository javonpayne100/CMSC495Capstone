import pygame
import random
import math
import time

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
# Question Pools
# ----------------------------

general_knowledge_questions = [
    {"question": "What is the capital of France?",
     "answers": ["Berlin", "Madrid", "Paris", "Rome"], "correct": 2},
    {"question": "Which country is known as the Land of the Rising Sun?",
     "answers": ["China", "South Korea", "Japan", "Thailand"], "correct": 2},
    {"question": "What is the largest country by area?",
     "answers": ["Russia", "Canada", "USA", "China"], "correct": 0},
    {"question": "How many continents are there?",
     "answers": ["5", "6", "7", "8"], "correct": 2},
    {"question": "Which ocean is the largest?",
     "answers": ["Atlantic", "Indian", "Pacific", "Arctic"], "correct": 2},
    {"question": "What is the longest river in the world?",
     "answers": ["Nile", "Amazon", "Yangtze", "Mississippi"], "correct": 0},
    {"question": "Which desert is the largest?",
     "answers": ["Sahara", "Arabian", "Gobi", "Kalahari"], "correct": 0},
    {"question": "Which country gifted the Statue of Liberty to the USA?",
     "answers": ["France", "England", "Germany", "Canada"], "correct": 0},
    {"question": "Which city is known as the Big Apple?",
     "answers": ["Los Angeles", "New York", "Chicago", "San Francisco"], "correct": 1},
    {"question": "What is the world's smallest country by area?",
     "answers": ["Monaco", "Nauru", "Vatican City", "San Marino"], "correct": 2},
    # Add more questions 11 through 100 here
]

history_questions = [
    {"question": "Who was the first President of the USA?",
     "answers": ["Jefferson", "Washington", "Lincoln", "Roosevelt"], "correct": 1},
    {"question": "In which year did World War II end?",
     "answers": ["1939", "1945", "1918", "1965"], "correct": 1},
    {"question": "Who led the nonviolent resistance in India?",
     "answers": ["Jinnah", "Gandhi", "Nehru", "Ambedkar"], "correct": 1},
    {"question": "What was the name of the ship that sank in 1912?",
     "answers": ["Lusitania", "Titanic", "Britannic", "Olympic"], "correct": 1},
    {"question": "Who was known as the Maid of Orléans?",
     "answers": ["Marie Antoinette", "Catherine de Medici", "Joan of Arc", "Eleanor of Aquitaine"], "correct": 2},
    {"question": "Which ancient civilization built the pyramids?",
     "answers": ["Greeks", "Romans", "Egyptians", "Mayans"], "correct": 2},
    {"question": "What wall divided East and West Berlin until 1989?",
     "answers": ["The Iron Curtain", "The Berlin Wall", "Hadrian's Wall", "The Great Wall"], "correct": 1},
    {"question": "Who was known as the Great Emancipator?",
     "answers": ["Abraham Lincoln", "Frederick Douglass", "Ulysses S. Grant", "Andrew Johnson"], "correct": 0},
    {"question": "In which year did the American Civil War begin?",
     "answers": ["1861", "1850", "1870", "1840"], "correct": 0},
    {"question": "Which emperor built the Colosseum?",
     "answers": ["Nero", "Marcus Aurelius", "Vespasian", "Caligula"], "correct": 2},
    # Add more questions 11 through 100 here
]

science_questions = [
    {"question": "What is the chemical symbol for water?",
     "answers": ["CO2", "H2O", "O2", "H2"], "correct": 1},
    {"question": "Which planet is known as the Red Planet?",
     "answers": ["Earth", "Mars", "Jupiter", "Saturn"], "correct": 1},
    {"question": "What gas do plants absorb from the atmosphere?",
     "answers": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "correct": 1},
    {"question": "What is the hardest natural substance on Earth?",
     "answers": ["Gold", "Iron", "Diamond", "Platinum"], "correct": 2},
    {"question": "Which organelle is known as the powerhouse of the cell?",
     "answers": ["Nucleus", "Mitochondria", "Chloroplast", "Ribosome"], "correct": 1},
    {"question": "What is the primary gas found in the Earth's atmosphere?",
     "answers": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"], "correct": 1},
    {"question": "Which part of the atom has no electric charge?",
     "answers": ["Electron", "Proton", "Neutron", "Nucleus"], "correct": 2},
    {"question": "What force keeps us on the ground?",
     "answers": ["Magnetism", "Friction", "Gravity", "Inertia"], "correct": 2},
    {"question": "At what temperature does water freeze (Celsius)?",
     "answers": ["0°", "32°", "100°", "–10°"], "correct": 0},
    {"question": "Which element is represented by the symbol 'O'?",
     "answers": ["Oxygen", "Gold", "Osmium", "Hydrogen"], "correct": 0},
    # Add more questions 11 through 100 here.
]

# Combine question pools into a dictionary
categories = {
    "General Knowledge": general_knowledge_questions,
    "History": history_questions,
    "Science": science_questions,
}


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
    input_boxes = [
        pygame.Rect(SCREEN_WIDTH // 2 - 150, 100, 300, 50),
        pygame.Rect(SCREEN_WIDTH // 2 - 150, 200, 300, 50),
    ]
    active_box = 0
    texts = ["", ""]
    box_colors = [WHITE, WHITE]
    running = True
    while running:
        screen.fill(BLACK)
        render_text("Enter Player Names", SCREEN_WIDTH // 2 - 120, 30, font, YELLOW)
        render_text("Press ENTER to start!", SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT - 50, font, WHITE)
        for i, box in enumerate(input_boxes):
            pygame.draw.rect(screen, box_colors[i], box, 2)
            text_surface = font.render(texts[i], True, WHITE)
            screen.blit(text_surface, (box.x + 10, box.y + 10))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and all(texts):
                    players = texts
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    texts[active_box] = texts[active_box][:-1]
                else:
                    texts[active_box] += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(event.pos):
                        active_box = i
        box_colors = [WHITE if i != active_box else YELLOW for i in range(2)]
    if not players:
        players = ["Player 1", "Player 2"]


def select_category():
    screen.fill(BLACK)
    render_text("Select a Category:", 100, 50, font, WHITE)
    categories_list = list(categories.keys())
    for idx, cat in enumerate(categories_list):
        render_text(f"{idx + 1}. {cat}", 100, 150 + idx * 50, font, YELLOW)
    pygame.display.flip()
    selected_category = None
    while selected_category is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for idx, cat in enumerate(categories_list):
                    x = 100
                    y = 150 + idx * 50
                    text_width, text_height = font.size(f"{idx + 1}. {cat}")
                    if x <= mouse_x <= x + text_width and y <= mouse_y <= y + text_height:
                        selected_category = cat
                        break
    return selected_category


# ----------------------------
# Main Game Function
# ----------------------------
def trivia_game():
    stop_trivia_music()  # Ensure no music in menus
    add_player_screen()  # Collect player names
    selected_category = select_category()  # Select a category
    question_pool = categories[selected_category]  # Use the full question pool

    # Here we do not remove questions from the pool, so each player samples 5 questions from the full bank.
    # (Each player's 5 questions will be unique within their own session.)
    if len(question_pool) < 5:
        screen.fill(BLACK)
        render_text("Not enough questions in this category!", 50, SCREEN_HEIGHT // 2, font, RED)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        return

    play_trivia_music()  # Start gameplay music
    scores = {}  # Dictionary to store each player's session score

    # Each player gets exactly 5 unique random questions.
    for player in players:
        screen.fill(BLACK)
        render_text(f"{player}, press any key when ready!", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2, font, YELLOW)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False

        session_score = 0
        # Sample 5 random questions (unique within the session) without removing them from the global pool:
        session_questions = random.sample(question_pool, 5)

        clock = pygame.time.Clock()
        for question_data in session_questions:
            current_question = question_data["question"]
            answers = question_data["answers"]
            correct_index = question_data["correct"]
            time_left = 10.0  # Seconds per question
            answered = False
            while time_left > 0 and not answered:
                dt = clock.tick(60) / 1000.0  # Delta time in seconds
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit();
                        exit()
                screen.fill(BLACK)
                draw_background_gradient()
                render_text(f"{player}'s Turn", SCREEN_WIDTH // 2 - 100, 20, font, YELLOW)
                render_text(current_question, 50, 100, question_font, WHITE)
                start_y = 150
                for index, answer in enumerate(answers):
                    render_text(f"{index + 1}. {answer}", 50, start_y + index * 50, question_font, WHITE)
                    text_width, text_height = question_font.size(f"{index + 1}. {answer}")
                    x = 50
                    y = start_y + index * 50
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if x <= mouse_x <= x + text_width and y <= mouse_y <= y + text_height:
                        if pygame.mouse.get_pressed()[0]:
                            answered = True
                            if index == correct_index:
                                session_score += 1
                render_text(f"Score: {session_score}", SCREEN_WIDTH - 150, 20, font, GREEN)
                draw_timer((SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50), 40, time_left, 10)
                pygame.display.flip()
                if not answered:
                    time_left -= dt
        scores[player] = session_score
        screen.fill(BLACK)
        render_text(f"{player}'s round complete! Score: {session_score}", 100, SCREEN_HEIGHT // 2 - 50, font, YELLOW)
        render_text("Press any key for the next player's turn...", 100, SCREEN_HEIGHT // 2 + 50, font, WHITE)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False

    stop_trivia_music()  # Stop music after gameplay

    # Final results screen
    screen.fill(BLACK)
    render_text("Final Scores:", 100, 50, font, YELLOW)
    y_offset = 150
    for player, score in scores.items():
        render_text(f"{player}: {score}", 100, y_offset, font, WHITE)
        y_offset += 50
    winner = max(scores, key=scores.get)
    render_text(f"Winner: {winner}!", 100, y_offset + 50, font, GREEN)
    render_text("Press any key to exit.", 100, y_offset + 100, font, WHITE)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                waiting = False
    pygame.quit()


if __name__ == "__main__":
    trivia_game()
