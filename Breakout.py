import math
import pygame

# --- Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
magenta = (255, 0, 255)

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

        # Ball hitting the top wall
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
            return False  

        # Ball hitting the left wall
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
            return False  

        # Ball hitting the right wall
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
            return False  

        # Ball hitting the bottom (Game Over)
        if self.y > self.screenheight:
            return True  # Ball falls below the screen, game over

        return False  # Ball is still in play


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
    pygame.mouse.set_visible(1)  # Show cursor in menu
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


# --- Unified breakout_screen() ---
def breakout_screen(screen, font, wall_sound, paddle_sound, brick_sound, losing_sound):
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

    # Row colors
    row_colors = [red, green, blue, yellow, magenta]

    top = 80
    blockcount = 32

    for row in range(5):
        color = row_colors[row % len(row_colors)]
        for column in range(0, blockcount):
            block = Block(color, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        top += block_height + 2

    clock = pygame.time.Clock()
    game_over = False
    exit_program = False
    countdown_time = 5
    countdown_started = False
    countdown_start_ticks = 0
    losing_sound_played = False  # Flag to track if losing sound has played

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
            pygame.mouse.set_visible(1)  # Show cursor during countdown
            countdown_text = font.render(str(time_left), True, white)
            countdown_rect = countdown_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(countdown_text, countdown_rect)
        else:
            pygame.mouse.set_visible(0)  # Hide cursor during gameplay
            game_over = ball.update()
            player.update()

            if game_over:
                pygame.mouse.set_visible(1)  # Show cursor on Game Over
                text = font.render("Game Over", True, white)
                textpos = text.get_rect(centerx=screen.get_width() / 2)
                textpos.top = 300
                screen.blit(text, textpos)

                # Play the losing sound once when the game ends
                if not losing_sound_played:
                    losing_sound.play()
                    losing_sound_played = True  # Mark the sound as played

                # Back to Menu Button
                back_to_menu_button = pygame.Rect(250, 350, 300, 50)
                pygame.draw.rect(screen, white, back_to_menu_button)
                menu_text = font.render('Back to Menu', True, black)
                menu_text_rect = menu_text.get_rect(center=back_to_menu_button.center)
                screen.blit(menu_text, menu_text_rect)

                # Restart Button
                restart_button = pygame.Rect(250, 420, 300, 50)
                pygame.draw.rect(screen, white, restart_button)
                restart_text = font.render('Restart', True, black)
                restart_text_rect = restart_text.get_rect(center=restart_button.center)
                screen.blit(restart_text, restart_text_rect)

                if back_to_menu_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    return 'menu'
                if restart_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    return 'restart'

            if pygame.sprite.spritecollide(player, balls, False):
                diff = (player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2)
                ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
                ball.bounce(diff)
                paddle_sound.play()  # Play paddle hit sound

            deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
            if len(deadblocks) > 0:
                ball.bounce(0)
                brick_sound.play()  # Play brick hit sound
                if len(blocks) == 0:
                    game_over = True

        allsprites.draw(screen)
        pygame.display.flip()

    return 'exit'


# --- Main function ---
def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('Breakout Game')
    font = pygame.font.Font(None, 36)

    # Initialize mixer for sound
    pygame.mixer.init()

    # Load sounds
    wall_sound = pygame.mixer.Sound("wall.wav")
    paddle_sound = pygame.mixer.Sound("paddle.wav")
    brick_sound = pygame.mixer.Sound("brick.wav")
    losing_sound = pygame.mixer.Sound("mixkit-player-losing-or-failing-2042.wav")

    # Main menu loop
    while True:
        main_menu(screen, font)
        result = breakout_screen(screen, font, wall_sound, paddle_sound, brick_sound, losing_sound)
        if result == 'menu':
            continue
        elif result == 'exit':
            pygame.quit()
            break
        elif result == 'restart':
            continue  # Just loop back and restart


if __name__ == "__main__":
    main()
