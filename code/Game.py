import pygame

from code.Const import WIN_WITH, WIN_HEIGTH, MENU_OPTION
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WITH, WIN_HEIGTH))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()  # Close window
                quit()  # end pygame

            else:
                pass