import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


#criar janela do menu com imagem de background
class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        pygame.mixer_music.load('./asset/menu_ocean_sound.wav')  # adicionar música no menu
        pygame.mixer_music.play(-1)
        while True:

            self.window.blit(source=self.surf, dest=self.rect)  # manda a imagem para o retângulo da janela do menu
            self.menu_text(90, "Ocean", COLOR_ORANGE,((WIN_WIDTH / 2), 70)) # exibe o texto do menu
            self.menu_text(80, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            # texto exibição de opções do menu
            for i in range(len(MENU_OPTION)):
                self.menu_text(35, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()  # Close Window
                  quit()  # end pygame

    #desenhar o texto no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

