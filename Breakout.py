import os
import pygame
import random
import pyautogui

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
pygame.display.set_caption("Game Hub: Breakout")

# to control the frame rate/speed of the game
clock = pygame.time.Clock()
FPS = 70

# Initialize mixer for sound
pygame.mixer.init()

# Set volume (ensure the volume is not too low)
pygame.mixer.music.set_volume(1.0)

#Get path to directory where Breakout.py is located
BASE_DIR = os.path.dirname(__file__)
# Load sounds with error handling
try:
    wall_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "wall.wav"))
    paddle_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "paddle.wav"))
    brick_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "brick.wav"))
    losing_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "mixkit-player-losing-or-failing-2042.wav"))
except pygame.error as e:
    print("Error loading sound:", e)

# Striker class
class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.speed = speed
        self.color = color

        # The rect variable is used to handle the placement
        # and the collisions of the object
        self.strikerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.striker = pygame.draw.rect(screen, self.color, self.strikerRect)

    # Used to render the object on the screen
    def display(self):
        self.striker = pygame.draw.rect(screen, self.color, self.strikerRect)

    # Used to update the state of the object
    def update(self, xFac):
        self.posx += self.speed * xFac

        # Restricting the striker to be in between the left and right edges of the screen
        if self.posx <= 0:
            self.posx = 0
        elif self.posx + self.width >= WIDTH:
            self.posx = WIDTH - self.width

        self.strikerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    # Returns the rect of the object
    def getRect(self):
        return self.strikerRect

# Block Class
class Block:
    def __init__(self, posx, posy, width, height, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.color = color
        self.damage = 100

        # The white blocks have the health of 200. So, the ball must hit it twice to break
        if color == RED:
            self.health = 300
        elif color == BLUE:
            self.health = 200
        else:
            self.health = 100

        # The rect variable is used to handle the placement and the collisions of the object
        self.blockRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.block = pygame.draw.rect(screen, self.color, self.blockRect)

    # Used to render the object on the screen if and only if its health is greater than 0
    def display(self):
        if self.health > 0:
            self.brick = pygame.draw.rect(screen, self.color, self.blockRect)

    # Used to decrease the health of the block
    def hit(self):
        self.health -= self.damage

    # Used to get the rect of the object
    def getRect(self):
        return self.blockRect

    # Used to get the health of the object
    def getHealth(self):
        return self.health

# Ball Class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx, self.posy = posx, posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac, self.yFac = 1, 1

        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    # Used to display the object on the screen
    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    # Used to update the state of the object
    def update(self):
        self.posx += self.xFac * self.speed
        self.posy += self.yFac * self.speed

        # Reflecting the ball if it touches either of the vertical edges
        if self.posx <= 0 or self.posx >= WIDTH:
            self.xFac *= -1
            wall_sound.play()  # Play wall hit sound

        # Reflection from the top most edge of the screen
        if self.posy <= 0:
            self.yFac *= -1

        # If the ball touches the bottom most edge of the screen, True value is returned
        if self.posy >= HEIGHT:
            return True

        return False

    # Resets the position of the ball
    def reset(self):
        self.posx = 0
        self.posy = HEIGHT
        self.xFac, self.yFac = 1, -1

    # Used to change the direction along Y axis
    def hit(self):
        self.yFac *= -1
        paddle_sound.play()  # Play paddle hit sound

    # Returns the rect of the ball
    def getRect(self):
        return self.ball

# Function used to check collisions between any two entities
def collisionChecker(rect, ball):
    if pygame.Rect.colliderect(rect, ball):
        return True
    return False

# Function used to populate the blocks
def populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap):
    listOfBlocks = []
    for i in range(0, WIDTH, blockWidth + horizontalGap):
        for j in range(0, HEIGHT // 2, blockHeight + verticalGap):
            listOfBlocks.append(Block(i, j, blockWidth, blockHeight, random.choice([RED, BLUE, GREEN])))
    return listOfBlocks

# Once all the lives are over, this function will display buttons to play again or return to main menu
def gameOverScreen():
    button_font = pygame.font.Font(None, 36)
    restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 40)
    menu_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 30, 200, 40)

    while True:
        screen.fill(BLACK)

        # Get current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Determine button colors
        restart_color = (100, 255, 100) if restart_button.collidepoint(mouse_pos) else GREEN
        menu_color = (100, 100, 255) if menu_button.collidepoint(mouse_pos) else BLUE

        # Draw title
        title_text = button_font.render("Game Over!", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))

        # Draw buttons
        pygame.draw.rect(screen, restart_color, restart_button)
        pygame.draw.rect(screen, menu_color, menu_button)

        # Draw button text
        restart_text = button_font.render("Play Again", True, BLACK)
        menu_text = button_font.render("Main Menu", True, BLACK)
        screen.blit(restart_text, (restart_button.x + 30, restart_button.y + 5))
        screen.blit(menu_text, (menu_button.x + 35, menu_button.y + 5))

        pygame.display.update()
# event handler for buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"
                elif menu_button.collidepoint(event.pos):
                    return "menu"


def main():
    running = True
    lives = 3
    score = 0

    scoreText = font.render("score", True, WHITE)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (20, HEIGHT - 10)

    livesText = font.render("Lives", True, WHITE)
    livesTextRect = livesText.get_rect()
    livesTextRect.center = (120, HEIGHT - 10)

    striker = Striker(0, HEIGHT - 50, 100, 20, 10, WHITE)
    strikerXFac = 0

    ball = Ball(0, HEIGHT - 150, 7, 5, WHITE)

    blockWidth, blockHeight = 40, 15
    horizontalGap, verticalGap = 10, 10

    listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)

    # Game loop
    while running:
        screen.fill(BLACK)
        screen.blit(scoreText, scoreTextRect)
        screen.blit(livesText, livesTextRect)

        scoreText = font.render("Score : " + str(score), True, WHITE)
        livesText = font.render("Lives : " + str(lives), True, WHITE)

        # If all the blocks are destroyed, then we repopulate them
        if not listOfBlocks:
            listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)

        # All the lives are over. So, the gameOver() function is called
        if lives <= 0:
            # Play the losing sound when game ends
            losing_sound.play()
            result = gameOverScreen()

            if result == "restart":
                lives = 3
                score = 0
                listOfBlocks = populateBlocks(blockWidth, blockHeight,horizontalGap, verticalGap)
                continue # jumps back into loop
            elif result == "menu":
                return "menu"
            elif result == "quit":
                running = False
                break

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    strikerXFac = -1
                if event.key == pygame.K_RIGHT:
                    strikerXFac = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    strikerXFac = 0

        # Collision check
        if collisionChecker(striker.getRect(), ball.getRect()):
            ball.hit()

        for block in listOfBlocks:
            if collisionChecker(block.getRect(), ball.getRect()):
                ball.hit()
                block.hit()

                if block.getHealth() <= 0:
                    listOfBlocks.pop(listOfBlocks.index(block))
                    score += 5
                    brick_sound.play()  # Play brick hit sound

        # Update
        striker.update(strikerXFac)
        lifeLost = ball.update()

        # If the ball goes off the screen, a life is lost
        if lifeLost:
            lives -= 1
            ball.reset()

        # Display all blocks and entities
        for block in listOfBlocks:
            block.display()

        ball.display()
        striker.display()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    return "menu"

if __name__ == "__main__":
    result = main()
    if result == "menu":
        from MainMenu import main_menu
        main_menu()
