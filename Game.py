import sys
import pygame
import chess
import Home_Screen
import Win_Screen

WIDTH, HEIGHT = 640, 640
SQ = WIDTH // 8
LIGHT = (240, 217, 181)
DARK  = (181, 136, 99)
HIGHLIGHT = (0, 255, 0)


def draw_board(screen: pygame.Surface, board: chess.Board, sel, legal):
    """Render the entire board state."""
    colors = (LIGHT, DARK)
    font = pygame.font.SysFont("arial", 32, bold=True)

    for rank in range(8):
        for file in range(8):
            color = colors[(rank + file) % 2]
            rect = pygame.Rect(file * SQ, rank * SQ, SQ, SQ)
            pygame.draw.rect(screen, color, rect)

            square = chess.square(file, 7 - rank)
            piece  = board.piece_at(square)
            if piece:
                # Use piece symbol as simple text sprite
                txt = font.render(piece.symbol(), True, (0, 0, 0))
                txt_rect = txt.get_rect(center=rect.center)
                screen.blit(txt, txt_rect)

            # selection + legal move hints
            if sel == square:
                pygame.draw.rect(screen, HIGHLIGHT, rect, 3)
            if square in legal:
                pygame.draw.circle(screen, HIGHLIGHT, rect.center, 8)


def game_loop(screen: pygame.Surface):
    """Single game until checkmate or stalemate."""
    board = chess.Board()
    clock = pygame.time.Clock()
    selected = None
    legal = []

    while not board.is_game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                file = x // SQ
                rank = 7 - (y // SQ)
                square = chess.square(file, rank)

                if selected is None:
                    piece = board.piece_at(square)
                    if piece and piece.color == board.turn:
                        selected = square
                        legal = [m.to_square for m in board.legal_moves if m.from_square == square]
                else:
                    move = chess.Move(selected, square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected = None
                    legal = []

        draw_board(screen, board, selected, legal)
        pygame.display.flip()
        clock.tick(60)

    outcome = board.outcome()
    winner  = "White" if outcome.winner else "Black" if outcome.winner is not None else "Nobody"
    return winner


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Chess")

    state = "home"
    winner = None

    while True:
        if state == "home":
            choice = home_screen.show_home_screen(screen)
            if choice == "start":
                state = "game"
            else:
                pygame.quit(); sys.exit()

        elif state == "game":
            winner = game_loop(screen)
            state = "win"

        elif state == "win":
            _ = win_screen.show_win_screen(screen, winner)
            state = "home"


if __name__ == "__main__":
    main()