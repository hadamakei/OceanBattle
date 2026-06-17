import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1Bg':                    #criação background level 1
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1Bg{i}', (0, 0))) #rodar imagem no background
                    list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':                     #Criação jogador 1
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':                     # Criação jogador 2
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':                      #Criação inimigo 1
                return Enemy('Enemy1',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':                       # Criação inimigo 2
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))