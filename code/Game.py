from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu

import pygame

from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        # criar janela
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            #Seleção do menu
            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]: # Escolha opção de qual jogo
                player_score = [0,0]        # placar do jogador 1 e 2
                level = Level(self.window, 'level1', menu_return, player_score)  # implementa nível 1
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'level2', menu_return, player_score)         # implementa nível 2
                    level_return = level.run(player_score)
                    if level_return:                                                              # salva o placar
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:             # opção do menu de pontuação
                score.show()

            elif menu_return == MENU_OPTION[4]:             # opção do menu sair
                pygame.quit()  # Fechar janela
                quit()  # Encerrar pygame
            else:
                pass






