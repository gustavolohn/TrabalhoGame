#C
import pygame

COLOR_YELLOW = (255, 222, 89)
COLOR_WHITE = (255, 255, 255)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 2,
    'Level1Bg2': 3,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60
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

#W
WIN_WIDTH = 640
WIN_HEIGHT = 480