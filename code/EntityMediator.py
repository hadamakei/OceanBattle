from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):                  # verifica colisão e dimimui vida da entidade
            if ent.rect.right < 0:
                ent.health = 0



    @staticmethod
    def verify_collision(entity_list: list[Entity]):    
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):           # verifica vida da entidade e destroi
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
