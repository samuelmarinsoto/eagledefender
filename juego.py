

import pygame
import math

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
pygame.display.set_caption('Eagle Defender')
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Duración del cronómetro en milisegundos (1 minuto)
cronometro_duration = 60 * 1000  # 60,000 milisegundos = 1 minuto

# Variable para rastrear si el cronómetro está activo
cronometro_activo = True

# Fuente para mostrar el tiempo restante
fuente = pygame.font.Font(None, 36)
# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 182, 193)  # Color rosa

# Cronómetro
start_time = pygame.time.get_ticks()  # Obtener el tiempo de inicio en milisegundos
game_duration = 5 * 60 * 1000  # 5 minutos en milisegundos

rio = pygame.Surface((20, pygame.display.get_surface().get_height()))
rio.fill(BLUE)

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

cuadro_color = GREEN  # Por defecto, el cuadro es de color rojo
key_1_pressed = False
key_2_pressed = False
key_3_pressed = False


tiempo_actual = pygame.time.get_ticks()

tiempo_restante = max(0, cronometro_duration - (tiempo_actual - start_time))

espera_turno_texto = "Espera tu turno"
fuente_espera_turno = pygame.font.Font(None, 36)


max_cubos_por_color = 10
cubos_azules = 0
cubos_verdes = 0
cubos_rosados = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    key_input = pygame.key.get_pressed()

    texto_cubos = fuente.render(
        f"Azules: {max_cubos_por_color - cubos_azules}, Verdes: {max_cubos_por_color - cubos_verdes}, Rosados: {max_cubos_por_color - cubos_rosados}",
        True, (0, 0, 0))
    screen.blit(texto_cubos, (screen.get_width() - 250, screen.get_height() - 30))

    # Movemos el cuadrado con las teclas de flecha

    if tiempo_restante == 0:
        texto_espera_turno = fuente_espera_turno.render(espera_turno_texto, True, (0, 0, 0))
        screen.blit(texto_espera_turno, (screen.get_width() - 200, 10))

    # Movemos el cuadrado con las teclas de flecha
    if key_input[pygame.K_UP] and rojoy > 0 and tiempo_restante<=0:
        rojoy -= 4
    if key_input[pygame.K_DOWN] and rojoy + cubo_original.get_height() < rio.get_height() and tiempo_restante<=0:
        rojoy += 4
    if key_input[pygame.K_LEFT] and rojox > 0 and tiempo_restante<=0:
        rojox -= 4
    if key_input[pygame.K_RIGHT] and rojox + cubo_original.get_width() < screen.get_width() and tiempo_restante<=0:
        rojox += 4

    # Movemos el punto con las teclas W, A, S y D
    if key_input[pygame.K_w] and point_y > 0:
        point_y -= 4
    if key_input[pygame.K_s] and point_y < screen.get_height():
        point_y += 4
    if key_input[pygame.K_a] and point_x > 0:
        point_x -= 4
    if key_input[pygame.K_d] and point_x < screen.get_width():
        point_x += 4

    if key_input[pygame.K_l] and tiempo_restante<=0:
        player_angle += 2

    if key_input[pygame.K_k] and tiempo_restante<=0:
        if bullet is None:
            bullet = {
                'x': rojox + cubo_original.get_width() / 2,
                'y': rojoy + cubo_original.get_height() / 2,
                'dx': bullet_speed * math.cos(math.radians(player_angle)),
                'dy': -bullet_speed * math.sin(math.radians(player_angle)),
                'color': GREEN  # Cambia el color de la bola a verde
            }

    if key_input[pygame.K_j]:
        if bullet is None:
            bullet = {
                'x': rojox + cubo_original.get_width() / 2,
                'y': rojoy + cubo_original.get_height() / 2,
                'dx': bullet_speed * math.cos(math.radians(player_angle)),
                'dy': -bullet_speed * math.sin(math.radians(player_angle)),
                'color': BLUE  # Cambia el color de la bola a azul
            }

    if key_input[pygame.K_h]:
        if bullet is None:
            bullet = {
                'x': rojox + cubo_original.get_width() / 2,
                'y': rojoy + cubo_original.get_height() / 2,
                'dx': bullet_speed * math.cos(math.radians(player_angle)),
                'dy': -bullet_speed * math.sin(math.radians(player_angle)),
                'color': RED  # Cambia el color de la bola a rojo
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
        pygame.draw.circle(screen, bullet["color"], (int(bullet['x']), int(bullet['y'])), 5)

        # Comprobar colisión entre la bala y los cuadrados
        for cuadrado in cuadrados:
            cuadrado_rect = cuadrado['surface'].get_rect(topleft=(cuadrado['x'], cuadrado['y']))
            if cuadrado_rect.collidepoint(int(bullet['x']), int(bullet['y'])):
                cuadrados.remove(cuadrado)  # Eliminar el cuadrado si hay colisión

        # Eliminar la bala si está fuera de la pantalla
        if not (0 <= bullet['x'] < screen.get_width() and 0 <= bullet['y'] < screen.get_height()):
            bullet = None

    # Dibujar los cuadrados
    for cuadrado in cuadrados:
        cuadrado_surface = cuadrado['surface'].copy()
        cuadrado_surface.fill(cuadrado['color'])  # Usar el color almacenado en la estructura
        screen.blit(cuadrado_surface, (cuadrado['x'], cuadrado['y']))

    if key_input[pygame.K_q]:
        if cuadro_color == BLUE and cubos_azules < 200:
            nuevo_cuadro = {
                'surface': cubo_original.copy(),
                'x': point_x - cubo_original.get_width() / 2,
                'y': point_y - cubo_original.get_height() / 2,
                'color': cuadro_color  # Almacena el color actual
            }
            cuadrados.append(nuevo_cuadro)
            cubos_azules += 1
            print(cubos_azules)
        elif cuadro_color == GREEN and cubos_verdes < 200:
            nuevo_cuadro = {
                'surface': cubo_original.copy(),
                'x': point_x - cubo_original.get_width() / 2,
                'y': point_y - cubo_original.get_height() / 2,
                'color': cuadro_color  # Almacena el color actual
            }
            cuadrados.append(nuevo_cuadro)
            cubos_verdes += 1
        elif cuadro_color == PINK and cubos_rosados < 200:
            nuevo_cuadro = {
                'surface': cubo_original.copy(),
                'x': point_x - cubo_original.get_width() / 2,
                'y': point_y - cubo_original.get_height() / 2,
                'color': cuadro_color  # Almacena el color actual
            }
            cuadrados.append(nuevo_cuadro)
            cubos_rosados += 1


    if key_input[pygame.K_1]:
        cuadro_color = BLUE  # Cambiar el color del cuadro a azul
        key_1_pressed = True
        key_2_pressed = False
        key_3_pressed = False


    if key_input[pygame.K_2]:
        cuadro_color = GREEN  # Cambiar el color del cuadro a verde
        key_1_pressed = False
        key_2_pressed = True
        key_3_pressed = False

    if key_input[pygame.K_3]:
        cuadro_color = PINK  # Cambiar el color del cuadro a rosa
        key_1_pressed = False
        key_2_pressed = False
        key_3_pressed = True

    if cronometro_activo:
        # Obtener el tiempo actual en milisegundos
        tiempo_actual = pygame.time.get_ticks()

        # Calcular el tiempo restante
        tiempo_restante = max(0, cronometro_duration - (tiempo_actual - start_time))

        if tiempo_restante == 0:
            # Detener el cronómetro cuando se alcanza la duración deseada
            cronometro_activo = False

    # ...

    # Mostrar el tiempo restante en la pantalla
    tiempo_mostrar = tiempo_restante // 1000  # Convertir a segundos
    texto_tiempo = fuente.render(f"Tiempo restante: {tiempo_mostrar} s", True, BLUE)
    screen.blit(texto_tiempo, (10, 10))


    pygame.display.update()
    clock.tick(144)