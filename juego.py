import pygame
import math

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
pygame.display.set_caption('Eagle Defender')
clock = pygame.time.Clock()

rio = pygame.Surface((20, pygame.display.get_surface().get_height()))
rio.fill('Blue')

cubo_rojo = pygame.Surface((50, 50))
cubo_rojo.fill('Red')

bola = pygame.Surface((10, 10))  # Superficie para representar la bola
bola.fill('Green')  # Cambia el color de la bola según tus preferencias

rojox = 550
rojoy = 300
player_angle = 0  # Ángulo de rotación del jugador
bullet = None  # Variable para representar el proyectil
bullet_speed = 5  # Velocidad del proyectil

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_w]:
        rojoy -= 4
    if key_input[pygame.K_s]:
        rojoy += 4
    if key_input[pygame.K_a]:
        rojox -= 4
    if key_input[pygame.K_d]:
        rojox += 4

    # Rotar el jugador suavemente
    if key_input[pygame.K_l]:
        player_angle += 2  # Ajusta la velocidad de rotación según tus preferencias

    # Disparar una única bola cuando se presiona la tecla "K"
    if key_input[pygame.K_k]:
        if bullet is None:
            bullet = {
                'x': rojox + cubo_rojo.get_width() / 2,
                'y': rojoy + cubo_rojo.get_height() / 2,
                'dx': bullet_speed * math.cos(math.radians(player_angle)),
                'dy': -bullet_speed * math.sin(math.radians(player_angle))
            }

    # Actualizar la posición del jugador en función del ángulo de rotación
    player_x = rojox + cubo_rojo.get_width() / 2
    player_y = rojoy + cubo_rojo.get_height() / 2
    rotated_cubo = pygame.transform.rotate(cubo_rojo, player_angle)
    player_rect = rotated_cubo.get_rect(center=(player_x, player_y))

    # Dibujar el jugador rotado en la pantalla
    screen.fill((255, 255, 255))
    screen.blit(rio, ((pygame.display.get_surface().get_width() // 2) - 10, 0))
    screen.blit(rotated_cubo, player_rect.topleft)

    # Dibujar la bola si está en vuelo
    if bullet:
        bullet['x'] += bullet['dx']
        bullet['y'] += bullet['dy']
        pygame.draw.circle(screen, (0, 255, 0), (int(bullet['x']), int(bullet['y'])), 5)
        # Verifica si la bola está fuera de la pantalla y resetea la variable
        if not (0 <= bullet['x'] < screen.get_width() and 0 <= bullet['y'] < screen.get_height()):
            bullet = None

    pygame.display.update()
    clock.tick(144)