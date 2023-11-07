import time
import pygame
from jugadorclase import Jugador
import spot

class Juego:
    def __init__(self, j1, j2):
        pygame.init()
        self.pantalla = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
        pygame.display.set_caption('Eagle Defender')

        img = pygame.image.load("../assets/Scenary/Arena Tileset Template Verde.png").convert()
        self.fondo = pygame.transform.scale(img, (self.pantalla.get_width(), self.pantalla.get_height()))
        
        self.clock = pygame.time.Clock()

        self.cron = 30000 # 30 segundos, por ahora
        self.pausa = False # estado de pausa. tecla "y" es pausa para ambos jugadores

        # van a ser objetos usuario con info del usuario
        self.j1 = j1
        self.j2 = j2
        self.cancion_def = None
        self.cancion_atq = None

        self.puntos_atacante = 0
        self.puntos_defensa = 0
        self.aguila_viva = 1

        self.balas = []
        self.barreras = []

    def seleccion_cancion(self, partida):
        if partida == 1:
            self.cancion_def = self.j1.song1
            self.cancion_atq = self.j2.song1
        elif partida == 2:
            self.cancion_def = self.j2.song1
            self.cancion_atq = self.j1.song1
        elif partida == 3:
            self.cancion_def = self.j1.song2
            self.cancion_atq = self.j2.song2
        elif partida == 4:
            self.cancion_def = self.j2.song2
            self.cancion_atq = self.j1.song2
        elif partida == 5:
            self.cancion_def = self.j1.song3
            self.cancion_atq = self.j2.song3
        elif partida == 6:
            self.cancion_def = self.j2.song3
            self.cancion_atq = self.j1.song3

    def cancionycron(self, cancion):
        spot.SearchSong(cancion)
        spot.PlaySong(spot.Song1)
        self.cron = spot.Song1All['duration_ms']
        
    # calcula tamano de puente en base a procentaje
    # de pantalla que ocupa
    def tamano_fuente(self, porcentaje):
        w = self.pantalla.get_width()
        h = self.pantalla.get_height()
        min_dim = min(w, h)
        return int(min_dim * porcentaje / 100)

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

    def blitpausa(self):
        tamano = self.tamano_fuente(12)
        fuente = pygame.font.Font(None, tamano)
        dim = fuente.size("Pausado")
        sup = fuente.render("Pausado", True, (0,0,0))
        w = self.pantalla.get_width()//2 - dim[0]//2
        h = self.pantalla.get_height()//2 - dim[1]//2

        self.pantalla.blit(sup, (w, h))
        pygame.display.update()
        
    def transicion(self, partida):
        tamano = self.tamano_fuente(12)
        fuente = pygame.font.Font(None, tamano)

        if partida > 1:
            dim = fuente.size("Cambio de rol!!!")
            sup = fuente.render("Cambio de rol!!!", True, (0,0,0))
            
            w = self.pantalla.get_width()//2 - dim[0]//2
            h = self.pantalla.get_height()//2 - dim[1]//2

            ut = time.time()
            
            while time.time() - ut < 3:
                self.pantalla.blit(sup, (w, h))
                pygame.display.update()
            
    def pausarmusica(self):
        if self.pausa:
            spot.PauseMusic()
        else:
            spot.unPauseMusic()
        
    def partida(self, partida):
        atacante = Jugador(1, partida, self.pantalla)
        defensor = Jugador(0, partida, self.pantalla)

        self.seleccion_cancion(partida)
        
        self.puntos_atacante = 0
        self.puntos_defensa = 0
        self.aguila_viva = 1

        self.balas = []
        self.barreras = []
        
        tamanocron = self.tamano_fuente(10) # 1/25 de la pantalla
        fcron = pygame.font.Font(None, tamanocron)

        tamanonom = self.tamano_fuente(5)
        fnom = pygame.font.Font(None, tamanonom)

        imgescala = self.pantalla.get_height()//5

        if partida%2:
            nombreD = self.j1.Username
            jachaD = pygame.image.load(self.j1.pathimage).convert_alpha()
            jachaD = pygame.transform.scale(jachaD, (imgescala, imgescala))
            jachaDC = pygame.Surface((imgescala, imgescala), pygame.SRCALPHA)

            pygame.draw.circle(jachaDC, (255, 255, 255), (imgescala//2, imgescala//2), imgescala//2)
            jachaD.set_colorkey((0, 0, 0))  # Make black pixels transparent
            jachaDC.blit(jachaD, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

            nombreA = self.j2.Username
            jachaA = pygame.image.load(self.j2.pathimage).convert_alpha()
            jachaA = pygame.transform.scale(jachaA, (imgescala, imgescala))
            jachaAC = pygame.Surface((imgescala, imgescala), pygame.SRCALPHA)

            pygame.draw.circle(jachaAC, (255, 255, 255), (imgescala//2, imgescala//2), imgescala//2)
            jachaA.set_colorkey((0, 0, 0))  # Make black pixels transparent
            jachaAC.blit(jachaA, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            
        else:
            nombreD = self.j2.Username
            jachaD = pygame.image.load(self.j2.pathimage).convert_alpha()
            jachaD = pygame.transform.scale(jachaD, (imgescala, imgescala))
            jachaDC = pygame.Surface((imgescala, imgescala), pygame.SRCALPHA)

            pygame.draw.circle(jachaDC, (255, 255, 255), (imgescala//2, imgescala//2), imgescala//2)
            jachaD.set_colorkey((0, 0, 0))  # Make black pixels transparent
            jachaDC.blit(jachaD, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

            nombreA = self.j1.Username
            jachaA = pygame.image.load(self.j1.pathimage).convert_alpha()
            jachaA = pygame.transform.scale(jachaA, (imgescala, imgescala))
            jachaAC = pygame.Surface((imgescala, imgescala), pygame.SRCALPHA)

            pygame.draw.circle(jachaAC, (255, 255, 255), (imgescala//2, imgescala//2), imgescala//2)
            jachaA.set_colorkey((0, 0, 0))  # Make black pixels transparent
            jachaAC.blit(jachaA, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

        self.cancionycron(self.cancion_def)

        self.transicion(partida)
        
        ultimo_tiempo = time.time()

        while self.cron > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    spot.PauseMusic()
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        self.pausa = not self.pausa  # Toggle the paused state
                        self.pausarmusica()
                        self.blitpausa()

            if self.pausa:
                ultimo_tiempo = time.time()
                continue
                
            # https://www.youtube.com/watch?v=OmkAUzvwsDk
            dt = time.time() - ultimo_tiempo
            ultimo_tiempo = time.time()

            # el fondo siempre se pone primero,
            # sino no se ve nada
            self.pantalla.blit(self.fondo, (0,0))

            cron_texto = f"Tiempo para defensa: {int(self.cron//1000)}"
            cron_texto_dim = fcron.size(cron_texto)
            cron_sup = fcron.render(cron_texto, True, (0, 0, 0))
            self.pantalla.blit(cron_sup, ((self.pantalla.get_width()//2)-(cron_texto_dim[0]//2), 0))

            self.pantalla.blit(jachaDC, (self.pantalla.get_width()//45,0))
            centraditoAC = self.pantalla.get_width()-imgescala-self.pantalla.get_width()//45
            self.pantalla.blit(jachaAC, (centraditoAC, 0))

            altura_nombres = self.pantalla.get_height()//4
            centradito_nombres = self.pantalla.get_width()//55
            atacante_centradito = self.pantalla.get_width() - centradito_nombres

            nomDdim = fnom.size(nombreD)
            nomDsup = fnom.render(nombreD, True, (0, 0, 0))
            self.pantalla.blit(nomDsup, (centradito_nombres, altura_nombres))

            nomAdim = fnom.size(nombreA)
            nomAsup = fnom.render(nombreA, True, (0, 0, 0))
            self.pantalla.blit(nomAsup, (atacante_centradito-nomAdim[0], altura_nombres))

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

            if defensor.check_termturno():
                self.cron = 0
        
        self.cancionycron(self.cancion_atq)

        while self.cron > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    spot.PauseMusic()
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        self.pausa = not self.pausa  # Toggle the paused state
                        self.pausarmusica()
                        self.blitpausa()

            if self.pausa:
                ultimo_tiempo = time.time()
                continue       

            dt = time.time() - ultimo_tiempo
            ultimo_tiempo = time.time()

            self.pantalla.blit(self.fondo, (0,0))
            
            cron_texto = f"Tiempo para ataque: {int(self.cron//1000)}"
            cron_texto_dim = fcron.size(cron_texto)
            cron_sup = fcron.render(cron_texto, True, (0, 0, 0))
            self.pantalla.blit(cron_sup, ((self.pantalla.get_width()//2)-(cron_texto_dim[0]//2), 0))

            self.pantalla.blit(jachaDC, (self.pantalla.get_width()//45,0))
            centraditoAC = self.pantalla.get_width()-imgescala-self.pantalla.get_width()//45
            self.pantalla.blit(jachaAC, (centraditoAC, 0))

            altura_nombres = self.pantalla.get_height()//4
            centradito_nombres = self.pantalla.get_width()//55
            atacante_centradito = self.pantalla.get_width() - centradito_nombres

            nomDdim = fnom.size(nombreD)
            nomDsup = fnom.render(nombreD, True, (0, 0, 0))
            self.pantalla.blit(nomDsup, (centradito_nombres, altura_nombres))

            nomAdim = fnom.size(nombreA)
            nomAsup = fnom.render(nombreA, True, (0, 0, 0))
            self.pantalla.blit(nomAsup, (atacante_centradito-nomAdim[0], altura_nombres))

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
            atacante.cambiar_sup()
            if nueva_bala:
                self.balas.append(nueva_bala)

            self.blittodo()
            self.pantalla.blit(defensor.sup, (defensor.posx, defensor.posy))
            self.pantalla.blit(atacante.sup, (atacante.posx, atacante.posy))
            atacante.dibujar_mira()

            self.clock.tick()
            pygame.display.update()

            self.cron -= dt*1000

            if atacante.check_termturno():
                self.cron = 0

        if self.aguila_viva:
            self.puntos_defensa = len(self.barreras)*2 + 1000
        else:
            self.puntos_defensa = len(self.barreras)*2

    def fin(self, puntos1, puntos2):

        tamano = self.tamano_fuente(12)
        fuente = pygame.font.Font(None, tamano)
        
        texto1 = f"{self.j1.Username}: {puntos1}"
        texto2 = f"{self.j2.Username}: {puntos2}"
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
            texto1 = "EMPATE!!! " + texto1 
            texto2 = "EMPATE!!! " + texto2
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

# TODO:
#
# sprint 2:
# seleccion de sprites, rotacion de bloques, animaciones de colision
#
# sprint 3:
# regeneracion con algoritmo de cocinero, salon de la fama
