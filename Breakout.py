import pygame
import random

pygame.init()
WIDTH, HEIGHT = 750, 450

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (51, 204, 51)
RED = (204, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 25)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 70

pygame.mixer.init()

# Load sounds
wall_sound = pygame.mixer.Sound("media/wall.wav")
paddle_sound = pygame.mixer.Sound("media/paddle.wav")
brick_sound = pygame.mixer.Sound("media/brick.wav")
losing_sound = pygame.mixer.Sound("media/mixkit-player-losing-or-failing-2042.wav")

class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx, self.posy = posx, posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.strikerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def display(self):
        pygame.draw.rect(screen, self.color, self.strikerRect)

    def move_keys(self, xFac):
        self.posx += self.speed * xFac
        self.posx = max(0, min(self.posx, WIDTH - self.width))
        self.strikerRect.x = self.posx

    def move_mouse(self):
        mouse_x = pygame.mouse.get_pos()[0]
        self.posx = mouse_x - self.width // 2
        self.posx = max(0, min(self.posx, WIDTH - self.width))
        self.strikerRect.x = self.posx

    def getRect(self):
        return self.strikerRect

class Block:
    def __init__(self, posx, posy, width, height, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.color = color
        self.damage = 100
        self.health = 300 if color == RED else 200 if color == BLUE else 100
        self.blockRect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def display(self):
        if self.health > 0:
            pygame.draw.rect(screen, self.color, self.blockRect)

    def hit(self):
        self.health -= self.damage

    def getRect(self):
        return self.blockRect

    def getHealth(self):
        return self.health

class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx, self.posy = posx, posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac, self.yFac = 1, 1

    def display(self):
        pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.xFac * self.speed
        self.posy += self.yFac * self.speed
        if self.posx <= 0 or self.posx >= WIDTH:
            self.xFac *= -1
            wall_sound.play()
        if self.posy <= 0:
            self.yFac *= -1
        return self.posy >= HEIGHT

    def reset(self):
        self.posx, self.posy = 0, HEIGHT
        self.xFac, self.yFac = 1, -1

    def hit(self):
        self.yFac *= -1
        paddle_sound.play()

    def getRect(self):
        return pygame.Rect(self.posx - self.radius, self.posy - self.radius, self.radius * 2, self.radius * 2)

def collisionChecker(rect, ball):
    return pygame.Rect.colliderect(rect, ball)

def populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap):
    return [Block(i, j, blockWidth, blockHeight, random.choice([RED, BLUE, GREEN]))
            for i in range(0, WIDTH, blockWidth + horizontalGap)
            for j in range(0, HEIGHT // 2, blockHeight + verticalGap)]

def draw_message(screen, message, font, box_color=(0, 0, 0), text_color=(255, 255, 255)):
    box_width, box_height = 500, 200
    box_x = (WIDTH - box_width) // 2
    box_y = (HEIGHT - box_height) // 2

    # Dim background
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    # Draw message box
    pygame.draw.rect(screen, box_color, (box_x, box_y, box_width, box_height))
    pygame.draw.rect(screen, text_color, (box_x, box_y, box_width, box_height), 3)

    # Render message (supports \n for multiple lines)
    lines = message.split("\n")
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, box_y + 40 + i * 30))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

    # Wait for keypress
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def gameOver():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "restart"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_m:
                    pygame.display.set_caption("Main Menu")
                    pygame.display.set_mode((600, 500))
                    return "main_menu"

def main():
    pygame.display.set_caption("Game Hub: Breakout")
    running = True
    lives = 3
    score = 0

    striker = Striker((WIDTH - 100) // 2, HEIGHT - 50, 100, 20, 10, WHITE)
    strikerXFac = 0

    ball = Ball(0, HEIGHT - 150, 7, 5, WHITE)
    listOfBlocks = populateBlocks(40, 15, 10, 10)

    draw_message(screen, "Move the paddle to hit the blocks with the ball.\nSome blocks make need more hits!\nKeys: < >, A D, Hold the mouse on paddle!\nPress any key to continue.", font)
    draw_message(screen, "You only have 3 lives!\nAnd it will keep track of your score!\nHave Fun!\nPress any key to continue.", font)

    while running:
        screen.fill(BLACK)

        screen.blit(font.render(f"Score: {score}", True, WHITE), (20, HEIGHT - 30))
        screen.blit(font.render(f"Lives: {lives}", True, WHITE), (120, HEIGHT - 30))

        if not listOfBlocks:
            listOfBlocks = populateBlocks(40, 15, 10, 10)

        if lives <= 0:
            draw_message(screen, "GAME OVER\nPress SPACE to restart\nESC to quit\nM for main menu", font)
            losing_sound.play()
            result = gameOver()
            if result == "restart":
                lives, score = 3, 0
                listOfBlocks = populateBlocks(40, 15, 10, 10)
                striker = Striker((WIDTH - 100) // 2, HEIGHT - 50, 100, 20, 10, WHITE)
            elif result == "main_menu":
                pygame.display.set_caption("Main Menu")
                pygame.display.set_mode((600, 500))
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    strikerXFac = -1
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    strikerXFac = 1
            if event.type == pygame.KEYUP and event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
                strikerXFac = 0

        if strikerXFac != 0:
            striker.move_keys(strikerXFac)
        elif pygame.mouse.get_focused() and pygame.mouse.get_pressed()[0]:
            striker.move_mouse()

        if collisionChecker(striker.getRect(), ball.getRect()):
            ball.hit()

        for block in listOfBlocks[:]:
            if collisionChecker(block.getRect(), ball.getRect()):
                ball.hit()
                block.hit()
                if block.getHealth() <= 0:
                    listOfBlocks.remove(block)
                    score += 5
                    brick_sound.play()

        if ball.update():
            lives -= 1
            ball.reset()

        striker.display()
        ball.display()
        for block in listOfBlocks:
            block.display()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
