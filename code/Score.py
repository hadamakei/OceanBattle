import datetime
import sys

import pygame
from pygame import Surface, Rect, KEYDOWN
from pygame.constants import K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import COLOR_ORANGE, SCORE_POS, COLOR_PURPLE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, COLOR_RED
from code.DBProxy import DBProxy



def get_formatted_date():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%d/%m/%Y")
    return f"{current_time} - {current_date}"


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/scoreBG.png').convert_alpha()    #adiciona imagem score
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode:str, player_score: list[int]):                     # Salva a pontuação
        pygame.mixer_music.load('./asset/score.wav')  # adicionar música no score
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')                               # conexão com bd
        name = ""
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(50, 'YOU WIN!!!', COLOR_PURPLE,SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:                         # jogo individual
                score = player_score[0]
                text = 'Player 1 enter your name(4 characters):'
            if game_mode == MENU_OPTION[1]:                             # jogo cooperativo
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name(4 characters):'
            if game_mode == MENU_OPTION[2]:                             # jogo competição
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name(4 characters):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name(4 characters):'
            self.score_text(25,text, COLOR_WHITE, SCORE_POS['EnterName'])
            for event in pygame.event.get():             #  checagem de eventos
                if event.type == pygame.QUIT:               # fechar a janela do jogo
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:                             # checa evento de teclado
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:                      #apaga o nome digitado
                        name = name[:-1]
                    else:                                                   # salva entrada de teclado na variável name
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(25, name, COLOR_WHITE, SCORE_POS['Name'])



            pygame.display.flip()
            pass

    def show(self):                                                # Exibe a pontuação na tela de score
        pygame.mixer_music.load('./asset/score.wav')  # adicionar música no score
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_RED, SCORE_POS['Title'])
        self.score_text(25, 'NAME       SCORE                      DATE     ', COLOR_ORANGE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(25, f'{name }     {score: 05d}     {date }', COLOR_YELLOW,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():             #  checagem de eventos
                if event.type == pygame.QUIT:               # fechar a janela do jogo
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    #Exibição dos textos
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)