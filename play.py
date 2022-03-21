import pygame, sys
import numpy as np

from constants import *
from draws import *
from logic import *


pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Roboto', SQUARE_SIZE//2)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))



draw_lines(screen)
player = 1
game_over = False

# pygame.draw.line(screen, CROSS_COLOR, (WIDTH//4, WIDTH//4), (WIDTH//3, WIDTH//3), CROSS_WIDTH)
                    
# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if avaibale_square(board, clicked_row, clicked_col):
                mark_square(board, clicked_row, clicked_col, player)
                if check_win(screen, board, player):
                    game_over = True
                player = player % 2 + 1
                draw_figures(screen, board)
                if is_board_full(board) and not check_win(screen, board, player):
                    screen.fill(BG_COLOR)
                    text = font.render('DRAW!', False, TEXT_COLOR)
                    screen.blit(text, (WIDTH//4, WIDTH//4))
                    # pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//4, WIDTH//2), CIRCLE_RADIUS//2, CIRCLE_WIDTH//2)
                    # pygame.draw.line(screen, CROSS_COLOR, (WIDTH//4+SPACE, WIDTH//4+SPACE), (SQUARE_SIZE+SQUARE_SIZE-SPACE, SQUARE_SIZE+SPACE), CROSS_WIDTH)
                    # pygame.draw.line(screen, CROSS_COLOR, (SQUARE_SIZE+SPACE, SQUARE_SIZE+SPACE), (SQUARE_SIZE+SQUARE_SIZE-SPACE, SQUARE_SIZE+SQUARE_SIZE-SPACE), CROSS_WIDTH)




        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player, board = restart(screen)
                game_over = False
            
    
    pygame.display.update()

