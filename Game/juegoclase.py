import pygame
from Game.jugadorclase import Jugador

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
        pygame.display.set_caption('Eagle Defender')

        self.fuente = pygame.font.Font(None, 36)
        
        self.clock = pygame.time.Clock()
        self.tiempo_inicio = pygame.time.get_ticks()

        self.cron_duracion = 1000*3

        self.atacante = Jugador(1, self.pantalla)
        self.defensor = Jugador(0, self.pantalla)

        self.fase = 0

    def cronometro(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_restante = self.cron_duracion + self.tiempo_inicio - tiempo_actual
        tiempo_restante //= 1000
        texto_tiempo = self.fuente.render(f"Tiempo restante: {tiempo_restante} s", True, (0,0,0))
        
        self.pantalla.blit(texto_tiempo, ((self.pantalla.get_width()//2)-150, 10))

        if tiempo_restante == 0:
            self.fase += 1
            self.tiempo_inicio = pygame.time.get_ticks()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # el fondo siempre se pone primero,
        # sino no se ve nada
        self.pantalla.fill((255, 255, 255))

        if self.fase > 0:
            self.atacante.moverse()
            
        self.defensor.moverse()
        self.pantalla.blit(self.atacante.sup, (self.atacante.posx, self.atacante.posy))
        self.pantalla.blit(self.defensor.sup, (self.defensor.posx, self.defensor.posy))

        self.cronometro()

        self.clock.tick(144)
        pygame.display.update()

juego = Juego()
while True:
    juego.run()

