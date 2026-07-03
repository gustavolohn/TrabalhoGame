import pygame

from code.Const import WIN_WITH, WIN_HEIGTH
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WITH, WIN_HEIGTH))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass