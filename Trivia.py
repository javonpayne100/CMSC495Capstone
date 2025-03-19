import pygame

def trivia_game():
    # Initialize a new pygame window
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Trivia Game")

    font = pygame.font.Font(None, 40)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    question = "What is the capital of France?"
    options = ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"]
    correct_answer = 3

    def render_text(text, x, y, color=WHITE):
        rendered_text = font.render(text, True, color)
        screen.blit(rendered_text, (x, y))

    # Main trivia game loop
    running = True
    while running:
        screen.fill(BLACK)

        render_text(question, 100, 50)
        for i, option in enumerate(options):
            render_text(option, 100, 150 + i * 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                option_clicked = (y - 150) // 50
                if option_clicked == correct_answer - 1:
                    print("Correct!")
                else:
                    print("Incorrect!")

        pygame.display.flip()

    pygame.quit()
