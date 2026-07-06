#C
import pygame
from pygame.examples.grid import WINDOW_WIDTH

COLOR_YELLOW = (255, 222, 89)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)
COLOR_BLACK = (0, 0, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 2,
    'Level1Bg2': 3,
    'Level2Bg0': 3,
    'Level2Bg1': 0,
    'Level2Bg2': 2,
    'Level2Bg3': 2,
    'Level2Bg4': 4,
    'Player1': 3,
    'Player1Shot': 5,
    'Player2': 3,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy2': 1,
    'Enemy1Shot': 5,
    'Enemy2Shot': 2

}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1':0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0

}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 200
}

#M
MENU_OPTION = ('Jogar',
               '1P - Competitive',
               '2P - Competitive',
               'Score',
               'Sair')

#P
PLAYER_KEY_UP = { 'Player1': pygame.K_UP,
                  'Player2': pygame.K_w}

PLAYER_KEY_RIGHT = { 'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

PLAYER_KEY_DOWN = { 'Player1': pygame.K_DOWN,
                    'Player2': pygame.K_s}

PLAYER_KEY_LEFT = { 'Player1': pygame.K_LEFT,
                    'Player2': pygame.K_a}

PLAYER_KEY_SHOOT = { 'Player1': pygame.K_RSHIFT,
                     'Player2': pygame.K_SPACE}

#S
SPAWN_TIME = 4000
SCORE_POS = {'Title': (WINDOW_WIDTH / 3, 150),
             'EnterName': (WINDOW_WIDTH / 3,170),
             'Label': (WINDOW_WIDTH / 3,200),
             'Name': (WINDOW_WIDTH / 3,220),
             0: (WINDOW_WIDTH / 3,220),
             1: (WINDOW_WIDTH / 3,240),
             2: (WINDOW_WIDTH / 3,260),
             3: (WINDOW_WIDTH / 3,280),
             4: (WINDOW_WIDTH / 3,300),
             5: (WINDOW_WIDTH / 3,320),
             6: (WINDOW_WIDTH / 3,340),
             7: (WINDOW_WIDTH / 3,360),
             8: (WINDOW_WIDTH / 3,380),
             9: (WINDOW_WIDTH / 3,400),
             }

#T

TIMEOUT_STEP = 100 #100ms

TIMEOUT_LEVEL = 60000 #60s

#W
WIN_WIDTH = 640
WIN_HEIGHT = 480