import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)  # construtor no jogador herdado do Entity
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self, ):  # movimentação do jogador
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # Subir o jogador até o limite do topo da tela
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[
            self.name]] and self.rect.bottom < WIN_HEIGHT:  # Descer o jogador até o limite da base da tela
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[
            PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Voltar o jogador até o limite da esquerda da tela
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[
            self.name]] and self.rect.right < WIN_WIDTH:  # Avançar o jogador até o limite da direita da tela
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):  # movimentação do tiro
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
