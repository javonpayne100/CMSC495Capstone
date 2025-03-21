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

# Load sounds
wall_sound = pygame.mixer.Sound("wall.wav")
paddle_sound = pygame.mixer.Sound("paddle.wav")
brick_sound = pygame.mixer.Sound("brick.wav")
losing_sound = pygame.mixer.Sound("mixkit-player-losing-or-failing-2042.wav")

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

# Once all the lives are over, this function waits until exit or space bar is pressed and does the corresponding action
def gameOver():
    gameOver = True
    while gameOver:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

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
            pyautogui.alert('Press SPACE to restart or quit!', "Game Over!")  # notification to instruct player
            # Play the losing sound when game ends
            losing_sound.play()
            running = gameOver()

            while listOfBlocks:
                listOfBlocks.pop(0)

            lives = 3
            score = 0
            listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)

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

        if lifeLost:
            lives -= 1
            ball.reset()
            print(lives)

        # Display
        striker.display()
        ball.display()

        for block in listOfBlocks:
            block.display()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
