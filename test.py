import pygame
from src.game.jugadorclase import Jugador

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w/2,pygame.display.Info().current_h/2))
pygame.display.set_caption('Eagle Defender')
clock = pygame.time.Clock()

rio = pygame.Surface((20,pygame.display.get_surface().get_height()))
rio.fill('Blue')

atacante = Jugador(1, screen)

tiempo_actual = pygame.time.get_ticks()
tiempo_inicio = pygame.time.get_ticks()
cron_duracion = 1000*60

tiempo_restante = max(0, cron_duracion - (tiempo_actual - tiempo_inicio))


fuente = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante = max(0, cron_duracion - (tiempo_inicio - tiempo_actual))
    tiempo_restante //= 1000
    texto_tiempo = fuente.render(f"Tiempo restante: {tiempo_restante} s", True, (255,255,255))
        
        
    atacante.moverse()

    clock.tick(144)
    screen.fill((0,0,0))
    screen.blit(texto_tiempo, (100, 100))
    screen.blit(rio,((pygame.display.get_surface().get_width()//2)-10,0))
    screen.blit(atacante.sup , (atacante.posx,atacante.posy))
    pygame.display.update()
