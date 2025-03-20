import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Paddle
paddle_width = 100
paddle_height = 10
paddle = pygame.Rect((SCREEN_WIDTH // 2 - paddle_width // 2, SCREEN_HEIGHT - 40), (paddle_width, paddle_height))

# Ball
ball_radius = 10
ball = pygame.Rect((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), (ball_radius * 2, ball_radius * 2))
ball_dx, ball_dy = 5, -5

# Bricks
brick_rows = 5
brick_cols = 8
brick_width = SCREEN_WIDTH // brick_cols
brick_height = 20
bricks = [pygame.Rect(col * brick_width, row * brick_height + 50, brick_width, brick_height)
          for row in range(brick_rows) for col in range(brick_cols)]

# Game loop
def breakout_screen():
    global ball_dx, ball_dy
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move paddle with keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-8, 0)
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.move_ip(8, 0)

        # Move ball
        ball.move_ip(ball_dx, ball_dy)

        # Ball collisions
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_dx = -ball_dx
        if ball.top <= 0:
            ball_dy = -ball_dy
        if ball.colliderect(paddle):
            ball_dy = -ball_dy

        # Brick collisions
        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_dy = -ball_dy
                break

        # Draw objects
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.ellipse(screen, RED, ball)
        for brick in bricks:
            pygame.draw.rect(screen, WHITE, brick)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
