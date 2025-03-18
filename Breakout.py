import math
import pygame

# --- Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# --- Block size
block_width = 23
block_height = 15

# --- Classes ---
class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ball(pygame.sprite.Sprite):
    speed = 10.0
    x = 0.0
    y = 180.0
    direction = 200
    width = 10
    height = 10

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self):
        direction_radians = math.radians(self.direction)
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0:
            self.bounce(0)
            self.y = 1
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
        if self.y > 600:
            return True
        else:
            return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = 0
        self.rect.y = self.screenheight - self.height

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width


# --- Main Menu ---
def main_menu(screen, font):
    waiting = True
    while waiting:
        screen.fill(black)
        text = font.render("Breakout - Click to Start", True, white)
        screen.blit(text, (150, 250))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


# --- Restart Game Function ---
def restart_game(screen, font):
    breakout_screen(screen, font)


# --- Unified breakout_screen() ---
def breakout_screen(screen, font):
    # --- Main breakout game ---
    background = pygame.Surface(screen.get_size())
    blocks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()

    player = Player()
    allsprites.add(player)

    ball = Ball()
    allsprites.add(ball)
    balls.add(ball)

    top = 80
    blockcount = 32

    for row in range(5):
        for column in range(0, blockcount):
            block = Block(blue, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        top += block_height + 2

    clock = pygame.time.Clock()
    game_over = False
    exit_program = False
    countdown_time = 5
    countdown_started = False
    countdown_start_ticks = 0

    while not exit_program:
        clock.tick(30)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True

        if not countdown_started:
            countdown_start_ticks = pygame.time.get_ticks()
            countdown_started = True

        elapsed_time = (pygame.time.get_ticks() - countdown_start_ticks) / 1000
        time_left = countdown_time - int(elapsed_time)

        if time_left > 0:
            countdown_text = font.render(str(time_left), True, white)
            countdown_rect = countdown_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(countdown_text, countdown_rect)
        else:
            game_over = ball.update()
            player.update()

            if game_over:
                text = font.render("Game Over", True, white)
                textpos = text.get_rect(centerx=screen.get_width() / 2)
                textpos.top = 300
                screen.blit(text, textpos)

                # Back to Menu Button
                back_to_menu_button = pygame.Rect(250, 350, 300, 50)  # Increased width
                pygame.draw.rect(screen, white, back_to_menu_button)
                menu_text = font.render('Back to Menu', True, black)
                menu_text_rect = menu_text.get_rect(center=back_to_menu_button.center)
                screen.blit(menu_text, menu_text_rect)

                # Restart Button
                restart_button = pygame.Rect(250, 420, 300, 50)  # Increased width
                pygame.draw.rect(screen, white, restart_button)
                restart_text = font.render('Restart', True, black)
                restart_text_rect = restart_text.get_rect(center=restart_button.center)
                screen.blit(restart_text, restart_text_rect)

                pygame.mouse.set_visible(1)
                if back_to_menu_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    exit_program = True
                if restart_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    restart_game(screen, font)

            if pygame.sprite.spritecollide(player, balls, False):
                diff = (player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2)
                ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
                ball.bounce(diff)

            deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
            if len(deadblocks) > 0:
                ball.bounce(0)
                if len(blocks) == 0:
                    game_over = True

        allsprites.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('Breakout Game')
    pygame.mouse.set_visible(0)
    font = pygame.font.Font(None, 36)

    main_menu(screen, font)
    breakout_screen(screen, font)
    pygame.quit()
