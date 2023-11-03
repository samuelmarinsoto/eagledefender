import pygame
import time
from jugadorclase import Jugador

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
        pygame.display.set_caption('Eagle Defender')

        img = pygame.image.load("Scenary/Arena Tileset Template Verde.png").convert()
        self.fondo = pygame.transform.scale(img, (self.pantalla.get_width(), self.pantalla.get_height()))
        
        self.clock = pygame.time.Clock()

        self.cron = 30000 # 30 segundos, por ahora

        # van a ser objetos usuario con info del usuario
        self.A = 0
        self.B = 0

        self.puntos_atacante = 0
        self.puntos_defensa = 0
        self.aguila_viva = 1

        self.balas = []
        self.barreras = []

    def colision(self):
        for barrera in self.barreras.copy():
            barrera_rect = barrera.sup.get_rect(topleft=(barrera.posx, barrera.posy))
            
            for bala in self.balas.copy():
                bala_rect = bala.sup.get_rect(topleft=(bala.posx, bala.posy))
                
                if barrera_rect.colliderect(bala_rect):
                    barrera.vida -= bala.vida
                    bala.sonido.play()
                    self.balas.remove(bala)

                    if barrera.vida <= 0:
                        barrera.sonido.play()
                        self.barreras.remove(barrera)
                        
                        self.puntos_atacante += 1
                        if barrera.tipo == 'X':
                            self.puntos_atacante += 1000
                            self.aguila_viva = 0
                            
                        break
                        
    def moverbalas(self, dt):
        for bala in self.balas:
            bala.moverse(dt)

    def blittodo(self):
        for bala in self.balas:
            self.pantalla.blit(bala.sup, (bala.posx, bala.posy))
        for barrera in self.barreras:
            self.pantalla.blit(barrera.sup, (barrera.posx, barrera.posy))
        
    def partida(self, partida):
        atacante = Jugador(1, partida, self.pantalla)
        defensor = Jugador(0, partida, self.pantalla)

        self.cron = 30000
        
        self.puntos_atacante = 0
        self.puntos_defensa = 0
        self.aguila_viva = 1

        self.balas = []
        self.barreras = []

        fuente = pygame.font.Font(None, 36)
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

            cron_texto = f"Tiempo para defensa: {self.cron//1000}"
            cron_texto_dim = fuente.size(cron_texto)
            cron_sup = fuente.render(cron_texto, True, (0, 0, 0))
            self.pantalla.blit(cron_sup, ((self.pantalla.get_width()//2)-(cron_texto_dim[0]//2), 0))

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
            self.cron -= dt*1000
        
        self.cron = 30000

        while self.cron > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            dt = time.time() - ultimo_tiempo
            ultimo_tiempo = time.time()

            self.pantalla.blit(self.fondo, (0,0))
            
            cron_texto = f"Tiempo para ataque: {self.cron//1000}"
            cron_texto_dim = fuente.size(cron_texto)
            cron_sup = fuente.render(cron_texto, True, (0, 0, 0))
            self.pantalla.blit(cron_sup, ((self.pantalla.get_width()//2)-(cron_texto_dim[0]//2), 0))

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

            self.cron -= dt*1000

        if self.aguila_viva:
            self.puntos_defensa = len(self.barreras)*2 + 1000
        else:
            self.puntos_defensa = len(self.barreras)*2

    def fin(self, puntos1, puntos2):

        fuente = pygame.font.Font(None, 144)
        
        texto1 = f"Jugador 1: {puntos1}"
        texto2 = f"Jugador 2: {puntos2}"
        texto1_dim = fuente.size(texto1)
        texto2_dim = fuente.size(texto2)
        texto1_color = (0,0,0)
        texto2_color = (0,0,0)

        if puntos1 > puntos2:
            texto1 = "GANADOR!!! " + texto1
            texto1_dim = fuente.size(texto1)
            texto1_color = (255,0,0)
        elif puntos2 > puntos1:
            texto2 = "GANADOR!!! " + texto2
            texto2_dim = fuente.size(texto2)
            texto2_color = (255,0,0)
        else:
            texto1 = "EMPATE!!!" + texto1 
            texto2 = "EMPATE!!!" + texto2
            texto1_dim = fuente.size(texto1)
            texto2_dim = fuente.size(texto2)
            texto1_color = (0,0,255)
            texto2_color = (0,0,255)

        texto1_sup = fuente.render(texto1, True, texto1_color)
        texto2_sup = fuente.render(texto2, True, texto2_color)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            self.pantalla.blit(texto1_sup, ((self.pantalla.get_width()//2) - (texto1_dim[0]//2), \
            (self.pantalla.get_height()//2) - (texto1_dim[1])))
            
            self.pantalla.blit(texto2_sup, ((self.pantalla.get_width()//2) - (texto2_dim[0]//2), \
            (self.pantalla.get_height()//2)))

            self.clock.tick()
            pygame.display.update()
        
        

def iniciar():
    jugador1_puntos = 0
    jugador2_puntos = 0
    
    juego = Juego()

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 1 iniciando")
    
    # match 1
    juego.partida(1)
    
    jugador1_puntos += juego.puntos_defensa
    jugador2_puntos += juego.puntos_atacante

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 2 iniciando")
    
    juego.partida(2)

    jugador1_puntos += juego.puntos_atacante
    jugador2_puntos += juego.puntos_defensa

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 3 iniciando")

    # match 2
    juego.partida(3)

    jugador1_puntos += juego.puntos_defensa
    jugador2_puntos += juego.puntos_atacante

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 4 iniciando")

    juego.partida(4)

    jugador1_puntos += juego.puntos_atacante
    jugador2_puntos += juego.puntos_defensa

    print("chequeando si fin")
    # chequea si ocupamos match 3
    if abs(jugador1_puntos - jugador2_puntos) >= 1000:
        juego.fin(jugador1_puntos, jugador2_puntos)

    else:
        print("no fin")

        print(jugador1_puntos)
        print(jugador2_puntos)
        print("partida 5 iniciando")
        
        # match 3
        juego.partida(5)

        jugador1_puntos += juego.puntos_defensa
        jugador2_puntos += juego.puntos_atacante

        print(jugador1_puntos)
        print(jugador2_puntos)
        print("partida 6 iniciando")

        juego.partida(6)

        jugador1_puntos += juego.puntos_atacante
        jugador2_puntos += juego.puntos_defensa

        print("fin, al fin")

        juego.fin(jugador1_puntos, jugador2_puntos)
    

iniciar()
# TODO:
# animaciones, musica, datos de usuario, regeneracion con algoritmo de cocinero, rotacion de bloques
