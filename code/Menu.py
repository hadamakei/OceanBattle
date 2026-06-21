import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, COLOR_DARK_BLUE, COLOR_PURPLE


# criar janela do menu com imagem de background
class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menuBG.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option: int = 0
        pygame.mixer_music.load('./asset/menu_ocean_sound.wav')  # adicionar música no menu
        pygame.mixer_music.play(-1)
        while True:
            # desenho das imagens
            self.window.blit(source=self.surf, dest=self.rect)  # manda a imagem para o retângulo da janela do menu
            self.menu_text(90, "Ocean", COLOR_PURPLE, ((WIN_WIDTH / 2), 70))  # exibe o texto do menu
            self.menu_text(80, "Battle", COLOR_PURPLE, ((WIN_WIDTH / 2), 120))

            # texto exibição de opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(35, MENU_OPTION[i], COLOR_YELLOW,
                                   ((WIN_WIDTH / 2), 180 + 30 * i))  # menu selecionado
                else:
                    self.menu_text(35, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))  # menu sem seleção
            pygame.display.flip()

            # Checagem dos eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # evento de fechar a janela
                    pygame.quit()  # Fechar janela
                    quit()  # Encerrar pygame
                if event.type == pygame.KEYDOWN:  # evento de apertar tecla
                    if event.key == pygame.K_DOWN:  # tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:  # altera seleção do menu
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # tecla para cima
                        if menu_option > 0:  # altera seleção do menu
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # tecla enter
                        return MENU_OPTION[menu_option]

    # desenhar o texto no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
