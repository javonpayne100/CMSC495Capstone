import pygame

def tbd_game():
    # Initialize a new pygame window
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("TBD Game")

    # Main game loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background (or leave it blank for clean slate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
