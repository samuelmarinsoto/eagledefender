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
                        
    def barrera_sobrelapa(self, pared):
        pared_rect = pared.sup.get_rect(topleft=(pared.posx, pared.posy))

        for barrera in self.barreras.copy():
            barrera_rect = barrera.sup.get_rect(topleft=(barrera.posx, barrera.posy))

            if barrera_rect.colliderect(pared_rect):
                return True
                
        return False
            
                        
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

    def blitstock(self, atacante, defensor):
        texto_madera = f"Madera: {defensor.balasA}"
        texto_acero = f"Acero: {defensor.balasB}"
        texto_concreto = f"Concreto: {defensor.balasC}"
        texto_agua = f"Agua: {atacante.balasA}"
        texto_fuego = f"Fuego: {atacante.balasB}"
        texto_bomba = f"Tierra: {atacante.balasC}"

        tamano_texto = self.tamano_fuente(5)
        ftexto = pygame.font.Font(None, tamano_texto)

        madera_dim = ftexto.size(texto_madera)
        madera_sup = ftexto.render(texto_madera, True, (0, 0, 0))
        acero_dim = ftexto.size(texto_acero)
        acero_sup = ftexto.render(texto_acero, True, (0, 0, 0))
        concreto_dim = ftexto.size(texto_concreto)
        concreto_sup = ftexto.render(texto_concreto, True, (0, 0, 0))
        
        agua_dim = ftexto.size(texto_agua)
        agua_sup = ftexto.render(texto_agua, True, (0, 0, 0))
        fuego_dim = ftexto.size(texto_fuego)
        fuego_sup = ftexto.render(texto_fuego, True, (0, 0, 0))
        bomba_dim = ftexto.size(texto_bomba)
        bomba_sup = ftexto.render(texto_bomba, True, (0, 0, 0))

        ancho = self.pantalla.get_width()
        altura = self.pantalla.get_height()
   
        self.pantalla.blit(concreto_sup, (0, altura-concreto_dim[1]))
        self.pantalla.blit(acero_sup, (0, altura-concreto_dim[1]-acero_dim[1]))
        self.pantalla.blit(madera_sup, (0, altura-concreto_dim[1]-acero_dim[1]-madera_dim[1]))
        
        self.pantalla.blit(bomba_sup, (ancho-bomba_dim[0], altura-bomba_dim[1]))
        self.pantalla.blit(fuego_sup, (ancho-fuego_dim[0], altura-bomba_dim[1]-fuego_dim[1]))
        self.pantalla.blit(agua_sup, (ancho-agua_dim[0], altura-concreto_dim[1]-fuego_dim[1]-agua_dim[1]))
        
        
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

            self.blitstock(atacante, defensor)

            defensor.moverse(dt)
            nueva_pared = defensor.disparar()

            if nueva_pared:
                if not self.barrera_sobrelapa(nueva_pared):
                    self.barreras.append(nueva_pared)
                else:
                    if nueva_pared.tipo == 'A':
                        defensor.balasA += 1
                    elif nueva_pared.tipo == 'B':
                        defensor.balasB += 1
                    elif nueva_pared.tipo == 'C':
                        defensor.balasC += 1
                    elif nueva_pared.tipo == 'X':
                        defensor.balasX += 1
                
            self.blittodo()
            self.pantalla.blit(defensor.sup, (defensor.posx, defensor.posy))
            self.pantalla.blit(atacante.sup, (atacante.posx, atacante.posy))

            self.clock.tick()
            pygame.display.update()

            # si se acaba el tiempo, cambiar de fase
            self.cron -= dt*1000

            if defensor.check_termturno():
                self.cron = 0
            if not self.aguila_viva:
                self.cron = 0
        
        self.cancionycron(self.cancion_atq)
        primerdisparo = 1
        regenstart = 0
        
        if defensor.balasX > 0:
            self.barreras.append(defensor.forzar_aguila())

        atacante.cocinero(self.cancion_atq)
        defensor.cocinero(self.cancion_def)
        print(atacante.tiempo_regen)
        print(defensor.tiempo_regen)
        
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

            if len(self.balas) > 0:
                if primerdisparo:
                    regenstart = 1
                primerdisparo = 0

            if regenstart:
                atacante.regen() # regenerar balas con algoritmo de cocinero
                defensor.regen() # regenerar barreras con algoritmo de cocinero
                    
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

            self.blitstock(atacante, defensor)

            self.moverbalas(dt)
            self.colision()

            defensor.moverse(dt)

            nueva_pared = defensor.disparar()
            if nueva_pared:
                if not self.barrera_sobrelapa(nueva_pared):
                    self.barreras.append(nueva_pared)
                else:
                    if nueva_pared.tipo == 'A':
                        defensor.balasA += 1
                    elif nueva_pared.tipo == 'B':
                        defensor.balasB += 1
                    elif nueva_pared.tipo == 'C':
                        defensor.balasC += 1
                    elif nueva_pared.tipo == 'X':
                        defensor.balasX += 1

            atacante.moverse(dt)

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
            if not self.aguila_viva:
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
# terminar regeneracion con algoritmo de cocinero
# 
