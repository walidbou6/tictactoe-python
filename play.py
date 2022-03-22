import pygame, sys
import numpy as np

from constants import *
from draws import *
from logic import *
import time


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
                    # time.sleep(2)
                    # screen.fill(BG_COLOR)
                    # board = np.zeros((BOARD_ROWS, BOARD_COLS))
                    # text = font.render('WINNER!', False, TEXT_COLOR)
                    # screen.blit(text, (WIDTH//6, WIDTH//6))


                player = player % 2 + 1
                draw_figures(screen, board)
                if is_board_full(board) and not check_win(screen, board, player):
                    screen.fill(BG_COLOR)
                    text = font.render('DRAW!', False, TEXT_COLOR)
                    screen.blit(text, (WIDTH//4, WIDTH//4))
                    pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//2+3*SPACE//2, WIDTH//2+SPACE//2), CIRCLE_RADIUS, CIRCLE_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, start_pos=(SQUARE_SIZE, SQUARE_SIZE+3*SPACE//2), end_pos=(2*SQUARE_SIZE-2*SPACE, 2*SQUARE_SIZE-SPACE//2), width=CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, start_pos=(SQUARE_SIZE, 2*SQUARE_SIZE-SPACE//2), end_pos=(2*SQUARE_SIZE-2*SPACE, SQUARE_SIZE+3*SPACE//2), width=CROSS_WIDTH)




        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player, board = restart(screen)
                game_over = False
            
    
    pygame.display.update()

