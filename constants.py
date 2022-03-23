import pygame


WIDTH = 600
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
TEXT_COLOR = (84, 84, 84)

# sounds
pygame.mixer.init()
player1_sound = pygame.mixer.Sound("./assests/player1.wav")
player2_sound = pygame.mixer.Sound("./assests/player2.wav")
win_sound = pygame.mixer.Sound('./assests/win.wav')
draw_sound = pygame.mixer.Sound('./assests/draw.wav')

