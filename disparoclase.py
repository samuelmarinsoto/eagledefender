import math
import pygame

class Bala:
	def __init__(self, rol, tipo, pantalla, x, y, angulo):
	    self.pantalla = pantalla
	    self.posx = x
	    self.posy = y
	    self.angulo = angulo

	    self.rol = rol
	    self.tipo = tipo
	    
	    if self.rol:
	        if self.tipo == 'A':
	            img = pygame.image.load("agua.png").convert_alpha()
	            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 50, self.pantalla.get_height() // 50))
	            self.sonido = pygame.mixer.Sound("agua.opus")
	            self.vida = 3
	            
	        elif self.tipo == 'B':
	            img = pygame.image.load("fuego.png").convert_alpha()
	            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 50, self.pantalla.get_height() // 50))
	            self.sonido = pygame.mixer.Sound("fuego.opus")
	            self.vida = 5
	            
	        elif self.tipo == 'C':
	            img = pygame.image.load("bomba.png").convert_alpha()
	            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 50, self.pantalla.get_height() // 50))
	            self.sonido = pygame.mixer.Sound("bomba.opus")
	            self.vida = 10
	    else:
	        if self.tipo == 'A':
	            img = pygame.image.load("assets/Blocks/bloquemadera.png").convert_alpha()
	            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 25, self.pantalla.get_height() // 25))
	            self.sonido = pygame.mixer.Sound("madera.opus")
	            self.vida = 3

	        elif self.tipo == 'B':
	            img = pygame.image.load("assets/Blocks/bloquemetal.png").convert_alpha()
	            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 25, self.pantalla.get_height() // 25))
	            self.sonido = pygame.mixer.Sound("metal.opus")
	            self.vida = 5
	            
	        elif self.tipo == 'C':
	            img = pygame.image.load("assets/Blocks/bloqueconcreto.png").convert_alpha()
	            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 25, self.pantalla.get_height() // 25))
	            self.sonido = pygame.mixer.Sound("concreto.opus")
	            self.vida = 10
	            
	        elif self.tipo == 'X':
	            img = pygame.image.load("assets/Blocks/aguila.png").convert_alpha()
	            self.sup = pygame.transform.scale(img, (self.pantalla.get_height() // 25, self.pantalla.get_height() // 25))
	            self.sonido = pygame.mixer.Sound("aguila.opus")
	            self.vida = 1

	def moverse(self, dt):
	    self.posx += 700*dt*math.cos(math.radians(self.angulo))
	    self.posy += 700*dt*math.sin(math.radians(self.angulo))
