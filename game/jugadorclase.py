import time
import math
import pygame
from disparoclase import Bala

class Jugador:
    def __init__(self, rol, partida, pantalla):
    
        # le damos a la clase acceso a la pantalla de juego
        self.pantalla = pantalla

        self.angulo = 180
        self.fecha_ultima_bala = time.time()
        
        self.balasA = 10
        self.balasB = 10
        self.balasC = 10
        self.balasX = 1
                
        # rol es 0 o 1,
        # 0 == defensor, 1 == atacante
        self.rol = rol

        if self.rol: # 1 == True
            # aparece en medio del lado derecho
            self.posx = (self.pantalla.get_width() * (3/4))
            self.posy = self.pantalla.get_height() // 2

            self.csprite = []
            csprite_archivos = [0, 1, 2, 3, 4, 5]
            
            for i in csprite_archivos:
                img = pygame.image.load("../goblinSpriteWalk/tile00" + str(i) + ".png")
                img_surf = img.convert_alpha()
                img_flip = pygame.transform.flip(img_surf, True, False)
                imgx = imgy = self.pantalla.get_height() // 20 * 3
                img_scale = pygame.transform.scale(img_flip, (imgx, imgy))
                self.csprite.append(img_scale)

            self.dsprite = []
            dsprite_archivos = [4, 5, 6, 7, 8, 9]
            
            for i in dsprite_archivos:
                img = pygame.image.load("../goblinSpriteShoot/tile06" + str(i) + ".png")
                img_surf = img.convert_alpha()
                img_flip = pygame.transform.flip(img_surf, True, False)
                imgx = imgy = self.pantalla.get_height() // 20 * 3
                img_scale = pygame.transform.scale(img_flip, (imgx, imgy))
                self.dsprite.append(img_scale)

            estatico = pygame.image.load("../goblinSpriteWalk/tile100.png").convert_alpha()
            estatico = pygame.transform.flip(estatico, True, False)
            imgx = imgy = self.pantalla.get_height() // 20 * 3
            self.estatico = pygame.transform.scale(estatico, (imgx, imgy))

            self.sup = self.estatico

            self.cframe = 0
            self.dframe = 0
            self.fecha_ultimo_frame = time.time()
            self.danimacion_empezada = 0
            self.canimacion_empezada = 0
            self.caminando_estado = 0
            self.disparando_estado = 0

            # atacante solo puede estar en lado derecho
            self.limitexmin = self.pantalla.get_width()//2
            self.limitexmax = self.pantalla.get_width()
            self.limiteymin = 0
            self.limiteymax = self.pantalla.get_height()

            if partida%2:
                # atacante se mueve con las flechas
                self.arriba = pygame.K_UP
                self.izquierda = pygame.K_LEFT
                self.abajo = pygame.K_DOWN
                self.derecha = pygame.K_RIGHT

                # dispara con 7890
                self.disparoA = pygame.K_8 # agua
                self.disparoB = pygame.K_9 # fuego
                self.disparoC = pygame.K_0 # bomba
                self.disparoX = pygame.K_7 # nada
                self.rothorario = pygame.K_o # rotacion
                self.rotahorario = pygame.K_u # rotacion

            else:
                # atacante se mueve con WASD
                self.arriba = pygame.K_w
                self.izquierda = pygame.K_a
                self.abajo = pygame.K_s
                self.derecha = pygame.K_d

                # dispara con 1234
                self.disparoA = pygame.K_1 # agua
                self.disparoB = pygame.K_2 # fuego
                self.disparoC = pygame.K_3 # bomba
                self.disparoX = pygame.K_4 # nada
                self.rothorario = pygame.K_e # horario
                self.rotahorario = pygame.K_q # antihorario
            
        else:
            # aparece en medio del lado izquierdo
            self.posx = (self.pantalla.get_width() * (1/4))
            self.posy = self.pantalla.get_height() // 2 
            
            self.sup = pygame.Surface((10,10))
            self.sup.fill('Green')

            # defensor solo puede estar en lado izquierdo
            self.limitexmin = 0
            self.limitexmax = self.pantalla.get_width()//2
            self.limiteymin = 0
            self.limiteymax = self.pantalla.get_height()

            if partida%2:
                # defensor se mueve con WASD
                self.arriba = pygame.K_w
                self.izquierda = pygame.K_a
                self.abajo = pygame.K_s
                self.derecha = pygame.K_d

                # pone bloques con 1234
                self.disparoA = pygame.K_1 # madera
                self.disparoB = pygame.K_2 # acero
                self.disparoC = pygame.K_3 # concreto
                self.disparoX = pygame.K_4 # aguila
                self.rothorario = pygame.K_e # horario
                self.rotahorario = pygame.K_q # antihorario

            else:
                # defensor se mueve con las flechas
                self.arriba = pygame.K_UP
                self.izquierda = pygame.K_LEFT
                self.abajo = pygame.K_DOWN
                self.derecha = pygame.K_RIGHT

                # pone bloques con 7890
                self.disparoA = pygame.K_8 # madera
                self.disparoB = pygame.K_9 # acero
                self.disparoC = pygame.K_0 # concreto
                self.disparoX = pygame.K_7 # aguila
                self.rothorario = pygame.K_o # rotacion
                self.rotahorario = pygame.K_u # rotacion

    # solo usar con atacante
    def cambiar_sup(self):
        if time.time() - self.fecha_ultimo_frame > 0.1: # 100ms por cada frame
            if self.disparando_estado or self.danimacion_empezada:
                self.danimacion_empezada = 1
                self.fecha_ultimo_frame = time.time()
                
                self.sup = self.dsprite[self.dframe]
                self.dframe += 1

                if self.dframe > 5:
                    self.dframe = 0
                    self.danimacion_empezada = 0
                
            elif self.caminando_estado or self.canimacion_empezada:
                self.canimacion_empezada = 1
                self.fecha_ultimo_frame = time.time()

                self.sup = self.csprite[self.cframe]
                self.cframe += 1

                if self.cframe > 5:
                    self.cframe = 0
                    self.canimacion_empezada = 0
                
            else:
                self.sup = self.estatico 
        
    # solo usar con atacante
    def dibujar_mira(self):
        # Calculate the line's end position based on the cube's position
        mirax = self.posx + self.sup.get_width() // 2 + self.pantalla.get_height()//15 * math.cos(math.radians(self.angulo))
        miray = self.posy + self.sup.get_height() // 2 + self.pantalla.get_height()//15 * math.sin(math.radians(self.angulo))
        
        # dibuja una linea cafe
        pygame.draw.line(self.pantalla, (139, 69, 19), (self.posx + self.sup.get_width() // 2, self.posy + self.sup.get_height() // 2), (mirax, miray), self.pantalla.get_height()//100)
        
    def moverse(self, dt):
        tecla = pygame.key.get_pressed()
        teclas_caminar = [self.arriba, self.abajo, self.izquierda, self.derecha]
        
        for i in teclas_caminar:
            if tecla[i]:
                self.caminando_estado = 1
                break
            else:
                self.caminando_estado = 0
                
        if self.caminando_estado:
            if tecla[self.arriba] and self.posy > self.limiteymin:
                self.posy -= 300*dt
            if tecla[self.abajo] and self.posy + self.sup.get_height() < self.limiteymax:
                self.posy += 300*dt
            if tecla[self.izquierda] and self.limitexmin < self.posx:
                self.posx -= 300*dt
            if tecla[self.derecha] and self.limitexmax > self.posx + self.sup.get_width():
                self.posx += 300*dt
                
        if tecla[self.rothorario]:
            self.angulo += 1
        if tecla[self.rotahorario]:
            self.angulo -= 1
        
    def disparar(self):
        tecla = pygame.key.get_pressed()
        teclas_disparo = [self.disparoA, self.disparoB, self.disparoC, self.disparoX]

        for i in teclas_disparo:
            if tecla[i]:
                self.disparando_estado = 1
                break
            else:
                self.disparando_estado = 0

        if self.disparando_estado and time.time() - self.fecha_ultima_bala > 0.2: # 200ms
        
            if tecla[self.disparoA] and self.balasA > 0:
                self.balasA -= 1
                self.fecha_ultima_bala = time.time()
                bala = Bala(self.rol, 'A', self.pantalla, self.posx + self.sup.get_width()//2, self.posy + self.sup.get_height()//2, self.angulo)
                return bala
                
            elif tecla[self.disparoB] and self.balasB > 0:
                self.balasB -= 1
                self.fecha_ultima_bala = time.time()
                bala = Bala(self.rol, 'B', self.pantalla, self.posx + self.sup.get_width()//2, self.posy + self.sup.get_height()//2, self.angulo)
                return bala
                
            elif tecla[self.disparoC] and self.balasC > 0:
                self.balasC -= 1
                self.fecha_ultima_bala = time.time()
                bala = Bala(self.rol, 'C', self.pantalla, self.posx + self.sup.get_width()//2, self.posy + self.sup.get_height()//2, self.angulo)
                return bala
                
            elif tecla[self.disparoX] and self.balasX > 0:
                self.balasX -= 1
                self.fecha_ultima_bala = time.time()
                if self.rol == 0:
                    bala = Bala(self.rol, 'X', self.pantalla, self.posx + self.sup.get_width()//2, self.posy + self.sup.get_height()//2, self.angulo)
                    return bala
