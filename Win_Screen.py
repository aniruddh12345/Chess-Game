import pygame, sys

WHITE = (255, 255, 255)
BG    = (30, 30, 30)


def show_win_screen(screen: pygame.Surface, winner: str) -> str:
    """Display the result. Returns 'home' when the user clicks."""
    font_big   = pygame.font.SysFont("arial", 48, bold=True)
    font_small = pygame.font.SysFont("arial", 32)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # single button area
                if 200 <= x <= 440 and 350 <= y <= 410:
                    return "home"

        screen.fill(BG)
        msg = f"{winner} wins!"
        label = font_big.render(msg, True, WHITE)
        rect  = label.get_rect(center=(320, 200))
        screen.blit(label, rect)

        pygame.draw.rect(screen, WHITE, (200, 350, 240, 60), 2)
        btn_lbl = font_small.render("Return to Home", True, WHITE)
        screen.blit(btn_lbl, (220, 365))

        pygame.display.flip()
        clock.tick(60)