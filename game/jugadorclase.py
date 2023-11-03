import time
import pygame
from game.disparoclase import Bala

class Jugador:
    def __init__(self, rol, partida, pantalla):
    
        # le damos a la clase acceso a la pantalla de juego
        self.pantalla = pantalla

        self.angulo = 0
        self.fecha_ultima_bala = time.time()*1000
        
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

            img = pygame.image.load("goblinSpriteWalk/tile000.png").convert_alpha()
            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 20 * 3, self.pantalla.get_height() // 20 * 3))

            # atacante solo puede estar en lado derecho
            self.limitexmin = self.pantalla.get_width()//2
            self.limitexmax = self.pantalla.get_width()
            self.limiteymin = 0
            self.limiteymax = self.pantalla.get_height()

            if partida%2:
                # atacante se mueve con las flechas
                self.arriba = pygame.K_i
                self.izquierda = pygame.K_j
                self.abajo = pygame.K_k
                self.derecha = pygame.K_l

                # dispara con 7890
                self.disparoA = pygame.K_8 # agua
                self.disparoB = pygame.K_9 # fuego
                self.disparoC = pygame.K_0 # bomba
                self.disparoX = pygame.K_7 # nada
                self.rotacion = pygame.K_o # rotacion

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
                self.rotacion = pygame.K_q # rotacion
            
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
                self.rotacion = pygame.K_q # rotacion

            else:
                # defensor se mueve con las flechas
                self.arriba = pygame.K_i
                self.izquierda = pygame.K_j
                self.abajo = pygame.K_k
                self.derecha = pygame.K_l

                # pone bloques con 7890
                self.disparoA = pygame.K_8 # madera
                self.disparoB = pygame.K_9 # acero
                self.disparoC = pygame.K_0 # concreto
                self.disparoX = pygame.K_7 # aguila
                self.rotacion = pygame.K_o # rotacion
    
    def moverse(self, dt):
        tecla = pygame.key.get_pressed()

        if tecla[self.arriba] and self.posy > self.limiteymin:
            self.posy -= 300*dt
        if tecla[self.abajo] and self.posy + self.sup.get_height() < self.limiteymax:
            self.posy += 300*dt
        if tecla[self.izquierda] and self.limitexmin < self.posx:
            self.posx -= 300*dt
        if tecla[self.derecha] and self.limitexmax > self.posx + self.sup.get_width():
            self.posx += 300*dt
        if tecla[self.rotacion]:
            self.angulo += 5
        
    def disparar(self):
        tecla = pygame.key.get_pressed()

        if time.time()*1000 - self.fecha_ultima_bala > 200:
        
            if tecla[self.disparoA] and self.balasA > 0:
                self.balasA -= 1
                self.fecha_ultima_bala = time.time()*1000
                bala = Bala(self.rol, 'A', self.pantalla, self.posx, self.posy, self.angulo)
                return bala
                
            elif tecla[self.disparoB] and self.balasB > 0:
                self.balasB -= 1
                self.fecha_ultima_bala = time.time()*1000
                bala = Bala(self.rol, 'B', self.pantalla, self.posx, self.posy, self.angulo)
                return bala
                
            elif tecla[self.disparoC] and self.balasC > 0:
                self.balasC -= 1
                self.fecha_ultima_bala = time.time()*1000
                bala = Bala(self.rol, 'C', self.pantalla, self.posx, self.posy, self.angulo)
                return bala
                
            elif tecla[self.disparoX] and self.balasX > 0:
                self.balasX -= 1
                self.fecha_ultima_bala = time.time()*1000
                if self.rol == 0:
                    bala = Bala(self.rol, 'X', self.pantalla, self.posx, self.posy, self.angulo)
                    return bala
