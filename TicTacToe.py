import pygame
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (100, 200, 150)

# Fonts
FONT = pygame.font.Font(None, 60)
BUTTON_FONT = pygame.font.Font(None, 40)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game board (3x3 matrix)
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# Draw game grid
def draw_grid():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


# Draw X and O
def draw_marks():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)


# Mark cell (X = 1, O = 2)
def mark_cell(row, col, player):
    board[row][col] = player


# Check if cell is empty
def is_cell_empty(row, col):
    return board[row][col] == 0


# Check if the board is full (draw)
def is_board_full():
    return np.all(board != 0)


# Check win conditions
def check_win(player):
    for row in range(BOARD_ROWS):
        if np.all(board[row, :] == player):
            return True

    for col in range(BOARD_COLS):
        if np.all(board[:, col] == player):
            return True

    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False


# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_win(2):  # AI Wins
        return 1
    elif check_win(1):  # Player Wins
        return -1
    elif is_board_full():  # Draw
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


# AI Move using Minimax
def ai_move():
    best_score = -float("inf")
    best_move = None

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        mark_cell(best_move[0], best_move[1], 2)


# Display game result and show Play Again button
def display_result(message):
    global game_over
    game_over = True  # Freeze game state
    screen.fill(BG_COLOR)

    # Show result message
    text = FONT.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text, text_rect)

    # Draw Play Again button
    button_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 60)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)

    button_text = BUTTON_FONT.render("Play Again", True, TEXT_COLOR)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    pygame.display.update()

    wait_for_restart(button_rect)


# Wait for player to click Play Again button
def wait_for_restart(button_rect):
    global game_over
    while game_over:  # Wait for player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_rect.collidepoint(x, y):  # If button clicked
                    restart_game()
                    return


# Restart the game
def restart_game():
    global board, player_turn, game_over
    board = np.zeros((BOARD_ROWS, BOARD_COLS))  # Reset board data
    player_turn = 1  # Reset turn to player
    game_over = False  # Allow moves again
    screen.fill(BG_COLOR)  # Clear screen
    draw_grid()  # Redraw grid
    pygame.display.update()  # Refresh screen


def tic_tac_toe():
    # initialize game look and music
    pygame.display.set_caption("Tic Tac Toe (Player vs AI)")
    screen.fill(BG_COLOR)

    # Main loop
    draw_grid()
    player_turn = 1
    game_over = False

    if __name__ == "__main__":
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player_turn == 1:
                    x, y = event.pos
                    row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

                    if is_cell_empty(row, col):
                        mark_cell(row, col, 1)
                        draw_marks()
                        pygame.display.update()  # ensures screen refresh

                        if check_win(1):
                            display_result("You Win!")
                        elif is_board_full():
                            display_result("It's a Draw!")
                        else:
                            player_turn = 2  # Switch to AI

                if player_turn == 2 and not game_over:
                    ai_move()
                    draw_marks()

                    if check_win(2):
                        display_result("You Lose!")
                    elif is_board_full():
                        display_result("It's a Draw!")
                    else:
                        player_turn = 1  # Switch back to player

            pygame.display.update()


if __name__ == "__main__":
    tic_tac_toe()
