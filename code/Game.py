from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
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
            menu_return = menu.run()

            #Seleção do menu
            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]: # Escolha opção de qual jogo
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Fechar janela
                quit()  # Encerrar pygame
            else:
                pass






