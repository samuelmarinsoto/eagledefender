import pygame
from jugadorclase import Jugador

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
        pygame.display.set_caption('Eagle Defender')

        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()

        self.cronometro_duration = 1000*60
        self.cronometro_activo = True

        self.fuente = pygame.font.Font(None, 36)
        # Definir colores
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.PINK = (255, 182, 193)  # Color rosa
        self.BROWN = (139, 69, 19)
        self.rio = pygame.Surface((20, pygame.display.get_surface().get_height()))
        self.rio.fill(self.BLUE)

        self.atacante = Jugador(1, self.pantalla)
        self.defensor = Jugador(0, self.pantalla)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.atacante.moverse()
        self.defensor.moverse()
        self.pantalla.fill((255, 255, 255))
        self.pantalla.blit(self.atacante.sup, (self.atacante.posx, self.atacante.posy))
        self.pantalla.blit(self.defensor.sup, (self.defensor.posx, self.defensor.posy))
        self.clock.tick(144)
        pygame.display.update()

juego = Juego()
while True:
    juego.run()

