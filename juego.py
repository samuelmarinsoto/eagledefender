import pygame
import math

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
pygame.display.set_caption('Eagle Defender')
clock = pygame.time.Clock()

rio = pygame.Surface((20, pygame.display.get_surface().get_height()))
rio.fill('Blue')

cubo_original = pygame.Surface((50, 50))
cubo_original.fill('Red')
cubo_rojo = cubo_original.copy()

bola = pygame.Surface((10, 10))
bola.fill('Green')

rojox = 550
rojoy = 300
player_angle = 0
bullet = None
bullet_speed = 5

line_length = 40
line_width = 3

# Inicializamos las coordenadas del punto
point_x = 400
point_y = 300

# Lista para almacenar los cuadrados
cuadrados = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    key_input = pygame.key.get_pressed()

    # Movemos el cuadrado con las teclas de flecha
    if key_input[pygame.K_UP]:
        rojoy -= 4
    if key_input[pygame.K_DOWN]:
        rojoy += 4
    if key_input[pygame.K_LEFT]:
        rojox -= 4
    if key_input[pygame.K_RIGHT]:
        rojox += 4

    # Movemos el punto con las teclas W, A, S y D
    if key_input[pygame.K_w]:
        point_y -= 4
    if key_input[pygame.K_s]:
        point_y += 4
    if key_input[pygame.K_a]:
        point_x -= 4
    if key_input[pygame.K_d]:
        point_x += 4

    if key_input[pygame.K_l]:
        player_angle += 2

    if key_input[pygame.K_k]:
        if bullet is None:
            bullet = {
                'x': rojox + cubo_original.get_width() / 2,
                'y': rojoy + cubo_original.get_height() / 2,
                'dx': bullet_speed * math.cos(math.radians(player_angle)),
                'dy': -bullet_speed * math.sin(math.radians(player_angle))
            }

    player_x = rojox + cubo_original.get_width() / 2
    player_y = rojoy + cubo_original.get_height() / 2
    rotated_cubo = pygame.transform.rotate(cubo_original, player_angle)
    player_rect = rotated_cubo.get_rect(center=(player_x, player_y))

    screen.fill((255, 255, 255))
    screen.blit(rio, ((pygame.display.get_surface().get_width() // 2) - 10, 0))

    # Dibujar una línea más grande que indica la dirección del frente del cuadrado
    front_x = player_x + line_length * math.cos(math.radians(player_angle))
    front_y = player_y - line_length * math.sin(math.radians(player_angle))
    pygame.draw.line(screen, (255, 0, 0), (player_x, player_y), (front_x, front_y), line_width)

    # Utilizamos el cuadro original sin cambios de tamaño
    screen.blit(rotated_cubo, player_rect.topleft)

    # Dibujamos el punto
    pygame.draw.circle(screen, (0, 0, 255), (int(point_x), int(point_y)), 5)

    if bullet:
        bullet['x'] += bullet['dx']
        bullet['y'] += bullet['dy']
        pygame.draw.circle(screen, (0, 255, 0), (int(bullet['x']), int(bullet['y'])), 5)
        if not (0 <= bullet['x'] < screen.get_width() and 0 <= bullet['y'] < screen.get_height()):
            bullet = None

    # Dibujar los cuadrados
    for cuadrado in cuadrados:
        screen.blit(cuadrado['surface'], (cuadrado['x'], cuadrado['y']))

    if key_input[pygame.K_q]:
        # Cuando se presiona Q, agregamos un cuadrado a la lista en las coordenadas del punto
        nuevo_cuadrado = {
            'surface': cubo_original.copy(),
            'x': point_x - cubo_original.get_width() / 2,
            'y': point_y - cubo_original.get_height() / 2
        }
        cuadrados.append(nuevo_cuadrado)

    pygame.display.update()
    clock.tick(144)