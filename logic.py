import pygame
import numpy as np
from constants import *
from draws import *



def avaibale_square(board, row, col):
    return board[row][col] == 0

def is_board_full(board):
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if board[r][c]==0:
                return False
    return True

def check_win(screen, board, player):
    # ver check
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_ver_win_line(screen, col, player)
            return True
    
    # hoz check
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_hoz_win_line(screen, row, player)
            return True

    # desc check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal(screen, player)
        return True

    # asc check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal(screen, player)
        return True
    
    return False
    

def draw_ver_win_line(screen, col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT-15), 15)

def draw_hoz_win_line(screen, row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (15, posY), (WIDTH-15, posY), 15)


def draw_asc_diagonal(screen, player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15, 15), 15)

def draw_desc_diagonal(screen, player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (15, 15), (WIDTH-15, HEIGHT-15), 15)

def restart(screen):
    screen.fill(BG_COLOR)
    draw_lines(screen)
    player = 1
    board = np.zeros((BOARD_ROWS, BOARD_COLS))
    return player, board
    

def disp_winner(screen, board, player, font):
    draw_figures(screen, board)
    s = pygame.Surface((WIDTH, HEIGHT))  # the size of your rect
    s.set_alpha(220)                # alpha level
    s.fill(BG_COLOR)           # this fills the entire surface
    screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
    text = font.render('WINNER!', False, TEXT_COLOR)
    screen.blit(text, (WIDTH//6, WIDTH//6))

    if player==1:
        pygame.draw.circle(screen, CIRCLE_COLOR, (SQUARE_SIZE+SQUARE_SIZE//2, SQUARE_SIZE+SQUARE_SIZE//2), 3*CIRCLE_RADIUS//2, CIRCLE_WIDTH)
    elif player==2:
        pygame.draw.line(screen, CROSS_COLOR, (SQUARE_SIZE, SQUARE_SIZE+SQUARE_SIZE), (SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE), CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR, (SQUARE_SIZE, SQUARE_SIZE), (SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE+SQUARE_SIZE), CROSS_WIDTH)

