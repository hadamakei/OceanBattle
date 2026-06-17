from code.Background import Background
from code.Const import WIN_WIDTH


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
