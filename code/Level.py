import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN, COLOR_CYAN, \
    COLOR_ORANGE, COLOR_PURPLE, COLOR_DARK_BLUE, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # Instancia nível do jogo
        player = EntityFactory.get_entity('Player1')  # Instancia jogador 1
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:  # Instancia jogador 2
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Geração do evento do inimigo
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Checar condição de vitória

    def run(self, player_score: list[int]):
        pygame.mixer.music.load(f'./asset/{self.name}.wav')  # adiciona musica level1
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()  # taxa de atualização fps
        while True:
            clock.tick(60)
            for ent in self.entity_list:  # lista de entidades
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_PURPLE, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', COLOR_DARK_BLUE,
                                    (10, 45))
            for event in pygame.event.get():  # checagem de eventos
                if event.type == pygame.QUIT:  # fechar a janela do jogo
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:  # Gerar Inimigos
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:  # checar timeout passagem para level 2
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False  # verifica se o jogador morre e perde o jogo
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            # Exibir o texto dos nives
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE,
                            (10, 5))  # Tempo de duração da fase
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE,
                            (10, WIN_HEIGHT - 35))  # Exibe o fps do jogo
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE,
                            (10, WIN_HEIGHT - 20))  # quantas entidades criadas na tela
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)  # Colisões
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
