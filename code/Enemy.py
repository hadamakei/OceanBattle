from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)  # construtor do Enemy herdado do Entity
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self,):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # movimento do inimigos

    def shoot(self ): # movimento dos tiros
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            return EnemyShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))