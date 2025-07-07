import pygame, sys

WHITE = (255, 255, 255)
BG    = (30, 30, 30)


def show_home_screen(screen: pygame.Surface) -> str:
    """Draws the home menu. Returns 'start' or 'quit'."""
    font_big   = pygame.font.SysFont("arial", 48, bold=True)
    font_small = pygame.font.SysFont("arial", 32)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Play button
                if 220 <= x <= 420 and 250 <= y <= 310:
                    return "start"
                # Quit button
                if 220 <= x <= 420 and 350 <= y <= 410:
                    return "quit"

        screen.fill(BG)
        title = font_big.render("Python Chess", True, WHITE)
        screen.blit(title, (160, 120))

        pygame.draw.rect(screen, WHITE, (220, 250, 200, 60), 2)
        play_lbl = font_small.render("Play", True, WHITE)
        screen.blit(play_lbl, (300, 265))

        pygame.draw.rect(screen, WHITE, (220, 350, 200, 60), 2)
        quit_lbl = font_small.render("Quit", True, WHITE)
        screen.blit(quit_lbl, (300, 365))

        pygame.display.flip()
        clock.tick(60)