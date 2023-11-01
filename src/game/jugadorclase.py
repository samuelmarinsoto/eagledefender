import pygame

class Jugador:
    def __init__(self, rol, pantalla):
    
        # le damos a la clase acceso a la pantalla de juego
        self.pantalla = pantalla

        # rol es 0 o 1,
        # 0 == defensor, 1 == atacante
        if rol: # 1 == True
            # aparece en medio del lado derecho
            self.posx = (self.pantalla.get_width() * (3/4))
            self.posy = self.pantalla.get_height() // 2
            self.sup = pygame.Surface((50, 50))
            self.sup.fill('Red')

            # atacante solo puede estar en lado derecho
            self.limite = range(self.pantalla.get_width()//2, self.pantalla.get_width())

            # atacante se mueve con las flechas
            self.arriba = pygame.K_UP
            self.izquierda = pygame.K_LEFT
            self.abajo = pygame.K_DOWN
            self.derecha = pygame.K_RIGHT
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
            
    def moverse(self):
        tecla = pygame.key.get_pressed()

        if tecla[self.arriba] and self.posy > 0:
            self.posy -= 4
        if tecla[self.abajo] and self.posy + self.sup.get_height() < self.pantalla.get_height():
            self.posy += 4
        if tecla[self.izquierda] and self.posx in self.limite:
            self.posx -= 4
        if tecla[self.derecha] and self.posx + self.sup.get_width() in self.limite:
            self.posx += 4
