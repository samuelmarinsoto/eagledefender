import pygame
from disparoclase import Bala

class Jugador:
    def __init__(self, rol, pantalla):
    
        # le damos a la clase acceso a la pantalla de juego
        self.pantalla = pantalla

        # rol es 0 o 1,
        # 0 == defensor, 1 == atacante
        self.rol = rol

        if self.rol: # 1 == True
            # aparece en medio del lado derecho
            self.posx = (self.pantalla.get_width() * (3/4))
            self.posy = self.pantalla.get_height() // 2
            self.sup = pygame.Surface((50, 50))
            self.sup.fill('Red')

            # atacante solo puede estar en lado derecho
            self.limite = range(self.pantalla.get_width()//2, self.pantalla.get_width())

            # atacante se mueve con las flechas
            self.arriba = pygame.K_i
            self.izquierda = pygame.K_j
            self.abajo = pygame.K_k
            self.derecha = pygame.K_l
            self.disparoA = pygame.K_8
            self.disparoB = pygame.K_9
            self.displaroC = pygame.K_0
            
        else:
            # aparece en medio del lado izquierdo
            self.posx = (self.pantalla.get_width() * (1/4))
            self.posy = self.pantalla.get_height() // 2 
            self.sup = pygame.Surface((10,10))
            self.sup.fill('Green')

            # defensor solo puede estar en lado izquierdo
            self.limite = range(0, self.pantalla.get_width()//2)
            
            # defensor se mueve con WASD
            self.arriba = pygame.K_w
            self.izquierda = pygame.K_a
            self.abajo = pygame.K_s
            self.derecha = pygame.K_d
            self.disparoA = pygame.K_1
            self.disparoB = pygame.K_2
            self.disparoC = pygame.K_3
            
    def moverse(self, dt):
        tecla = pygame.key.get_pressed()

        if tecla[self.arriba] and self.posy > 0:
            self.posy -= 4*dt
        if tecla[self.abajo] and self.posy + self.sup.get_height() < self.pantalla.get_height():
            self.posy += 4*dt
        if tecla[self.izquierda] and self.posx in self.limite:
            self.posx -= 4*dt
        if tecla[self.derecha] and self.posx + self.sup.get_width() in self.limite:
            self.posx += 4*dt

    def disparar(self):
        tecla = pygame.key.get_pressed()

        if tecla[self.disparoA]:
            bala = Bala(self.rol, 'A')
            return bala
        elif tecla[self.disparoB]:
            bala = Bala(self.rol, 'B')
            return bala
        elif tecla[self.disparoC]:
            bala = Bala(self.rol, 'C')
            return bala
        
