import pygame, sys
import numpy as np



WIDTH = 500
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = SQUARE_SIZE//8
CROSS_WIDTH = SQUARE_SIZE//5
SPACE = SQUARE_SIZE//4

# rgb : red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (66, 66, 66)


pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Roboto', SQUARE_SIZE//2)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE*2), (WIDTH, SQUARE_SIZE*2), LINE_WIDTH)
    
    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE*2, 0), (SQUARE_SIZE*2, HEIGHT), LINE_WIDTH)

def draw_figures():
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(c*SQUARE_SIZE+SQUARE_SIZE//2), int(r*SQUARE_SIZE+SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[r][c] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (c*SQUARE_SIZE+SPACE, r*SQUARE_SIZE+SQUARE_SIZE-SPACE), (c*SQUARE_SIZE+SQUARE_SIZE-SPACE, r*SQUARE_SIZE+SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (c*SQUARE_SIZE+SPACE, r*SQUARE_SIZE+SPACE), (c*SQUARE_SIZE+SQUARE_SIZE-SPACE, r*SQUARE_SIZE+SQUARE_SIZE-SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player

def avaibale_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if board[r][c]==0:
                return False
    return True

def check_win(player):
    # ver check
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_ver_win_line(col, player)
            return True
    
    # hoz check
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_hoz_win_line(row, player)
            return True

    # desc check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal(player)
        return True

    # asc check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True
    
    return False
    

def draw_ver_win_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT-15), 15)

def draw_hoz_win_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (15, posY), (WIDTH-15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15, 15), 15)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (15, 15), (WIDTH-15, HEIGHT-15), 15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    global player, board
    player = 1
    board = np.zeros((BOARD_ROWS, BOARD_COLS))
    


draw_lines()
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

            if avaibale_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
                draw_figures()
                if is_board_full() and not check_win(player):
                    screen.fill(BG_COLOR)
                    text = font.render('DRAW!', False, TEXT_COLOR)
                    screen.blit(text, (SQUARE_SIZE, SQUARE_SIZE))
                    # pygame.draw.circle(screen, CIRCLE_COLOR, (SQUARE_SIZE, SQUARE_SIZE), CIRCLE_RADIUS, CIRCLE_WIDTH)
                    # pygame.draw.line(screen, CROSS_COLOR, (SQUARE_SIZE+SPACE, SQUARE_SIZE+SQUARE_SIZE-SPACE), (SQUARE_SIZE+SQUARE_SIZE-SPACE, SQUARE_SIZE+SPACE), CROSS_WIDTH)
                    # pygame.draw.line(screen, CROSS_COLOR, (SQUARE_SIZE+SPACE, SQUARE_SIZE+SPACE), (SQUARE_SIZE+SQUARE_SIZE-SPACE, SQUARE_SIZE+SQUARE_SIZE-SPACE), CROSS_WIDTH)




        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
            
    
    pygame.display.update()

