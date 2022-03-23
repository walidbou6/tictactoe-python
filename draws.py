import pygame
from constants import *



def mark_square(board, row, col, player):
    board[row][col] = player

def draw_lines(screen):
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE*2), (WIDTH, SQUARE_SIZE*2), LINE_WIDTH)
    
    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE*2, 0), (SQUARE_SIZE*2, HEIGHT), LINE_WIDTH)

def draw_figures(screen, board):
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (c*SQUARE_SIZE+SQUARE_SIZE//2, r*SQUARE_SIZE+SQUARE_SIZE//2), CIRCLE_RADIUS, CIRCLE_WIDTH)
                
            elif board[r][c] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (c*SQUARE_SIZE+SPACE, r*SQUARE_SIZE+SQUARE_SIZE-SPACE), (c*SQUARE_SIZE+SQUARE_SIZE-SPACE, r*SQUARE_SIZE+SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (c*SQUARE_SIZE+SPACE, r*SQUARE_SIZE+SPACE), (c*SQUARE_SIZE+SQUARE_SIZE-SPACE, r*SQUARE_SIZE+SQUARE_SIZE-SPACE), CROSS_WIDTH)
                
                

