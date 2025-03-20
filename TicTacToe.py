import pygame

# Initialize pygame
pygame.init()

# Colors and settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (28, 170, 156)
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 200  # Adjusted spacing between grid lines for better alignment

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Empty board (0 means empty, 1 means player 1, 2 means player 2)
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Function to draw the grid
def draw_lines():
    # Draw horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # Draw vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


# Function to draw the board (X and O)
def draw_figures():
    for row in range(3):
        for col in range(3):
            # Center the figures within the grid
            center_x = col * SPACE + SPACE // 2
            center_y = row * SPACE + SPACE // 2

            if board[row][col] == 1:  # Player 1 (X)
                pygame.draw.line(screen, WHITE, (center_x - 50, center_y - 50),
                                 (center_x + 50, center_y + 50), CROSS_WIDTH)
                pygame.draw.line(screen, WHITE, (center_x + 50, center_y - 50),
                                 (center_x - 50, center_y + 50), CROSS_WIDTH)
            elif board[row][col] == 2:  # Player 2 (O)
                pygame.draw.circle(screen, WHITE, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)


# Function to check if the player has won
def check_win():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return None


# Function to reset the board
def reset_board():
    global board
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# The main tic-tac-toe function to run the game
def tic_tac_toe():
    player = 1  # Player 1 starts
    running = True
    while running:
        screen.fill(BLACK)  # Fill the screen with black
        draw_lines()  # Draw the grid
        draw_figures()  # Draw X's and O's

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked_row = y // SPACE
                clicked_col = x // SPACE

                if board[clicked_row][clicked_col] == 0:  # If the cell is empty
                    board[clicked_row][clicked_col] = player
                    player = 3 - player  # Switch player (1 -> 2, 2 -> 1)

        winner = check_win()
        if winner:
            print(f"Player {winner} wins!")
            reset_board()

        pygame.display.update()  # Update the display

    pygame.quit()
