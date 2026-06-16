from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        # criar janela
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


