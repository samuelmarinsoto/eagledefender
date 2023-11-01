import pygame
import time
from jugadorclase import Jugador

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
        pygame.display.set_caption('Eagle Defender')

        img = pygame.image.load("Scenary/Arena Tileset Template Verde.png")
        self.fondo = pygame.transform.scale(img, (self.pantalla.get_width(), self.pantalla.get_height()))
        
        self.clock = pygame.time.Clock()

        self.cron = 10000 # 10 segundos, por ahora

        # van a ser objetos usuario con info del usuario
        self.A = 0
        self.B = 0

        self.balas = []
        self.barreras = []

    def colision(self):
        for barrera in self.barreras.copy():
            for bala in self.balas.copy():
                if barrera.sup.get_rect().colliderect(bala.sup.get_rect()):
                    barrera.vida -= bala.vida
                    bala.sonido()
                    self.balas.remove(bala)

                    if barrera.vida <= 0:
                        self.barreras.remove(barrera)
                        break
                        
    def moverbalas(self, dt):
        for bala in self.balas:
            bala.moverse(dt)

    def blittodo(self):
        for bala in self.balas:
            self.pantalla.blit(bala.sup, (bala.x, bala.y))
        for barrera in self.barreras:
            self.pantalla.blit(barrera.sup, (barrera.x, barrera.y))
        
    def partida(self):
        atacante = Jugador(1, self.pantalla)
        defensor = Jugador(0, self.pantalla)

        ultimo_tiempo = time.time()
        while self.cron > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            # https://www.youtube.com/watch?v=OmkAUzvwsDk
            dt = time.time() - ultimo_tiempo
            ultimo_tiempo = time.time()

            # el fondo siempre se pone primero,
            # sino no se ve nada
            self.pantalla.blit(self.fondo, (0,0))

            defensor.moverse(dt)
            nueva_pared = defensor.disparar()
            
            if nueva_pared:
                self.barreras.append(nueva_pared)

            self.blittodo()
            self.pantalla.blit(defensor.sup, (defensor.posx, defensor.posy))
            self.pantalla.blit(atacante.sup, (atacante.posx, atacante.posy))
            
            self.clock.tick()
            pygame.display.update()

            # si se acaba el tiempo, cambiar de fase
            self.cron -= dt

        self.cron = 10000

        ultimo_tiempo = time.time()
        while self.cron > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            dt = time.time() - ultimo_tiempo
            ultimo_tiempo = time.time()

            self.pantalla.blit(self.fondo, (0,0))

            self.moverbalas(dt)
            self.colision()

            defensor.moverse(dt)
            # defensor.regenerar() # regenerar barreras con algoritmo de cocinero
            nueva_pared = defensor.disparar()
            if nueva_pared:
                self.barreras.append(nueva_pared)

            atacante.moverse(dt)
            # atacante.regenerar() # regenerar balas con algoritmo de cocinero
            nueva_bala = atacante.disparar()
            if nueva_bala:
                self.balas.append(nueva_bala)

            self.blittodo()
            self.pantalla.blit(defensor.sup, (defensor.posx, defensor.posy))
            self.pantalla.blit(atacante.sup, (atacante.posx, atacante.posy))

            self.clock.tick()
            pygame.display.update()

            self.cron -= dt

        return atacante.puntaje, defensor.puntaje
        

juego = Juego()
while True:
    juego.partida()
