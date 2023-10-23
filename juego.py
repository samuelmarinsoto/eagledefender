import time

import pygame
import math

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w // 1.5, pygame.display.Info().current_h // 1.5))
pygame.display.set_caption('Eagle Defender')
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Duración del cronómetro en milisegundos (1 minuto)
cronometro_duration = 1000 *60  # 60,000 milisegundos = 1 minuto

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
BROWN = (139, 69, 19)

# Cronómetro
start_time = pygame.time.get_ticks()  # Obtener el tiempo de inicio en milisegundos


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
aguila = 0

q_key_held = False

pausa_text_width = 200
pausa_text_height = 50
pausa_text_x = (screen.get_width() - pausa_text_width) // 2
pausa_text_y = (screen.get_height() - pausa_text_height) // 2

# Color del aviso de pausa
pausa_text_color = RED
pausado = False


def draw_color_boxes(screen, max_boxes, blue_count, green_count, pink_count, brown_count):
    box_size = 30
    margin = 10
    box_x = margin
    box_y = screen.get_height() - (max_boxes * (box_size + margin) + margin)

    # Dibujar cuadros de colores

    # Mostrar el texto indicador
    font = pygame.font.Font(None, 24)
    text = f"Azul: {max_boxes - blue_count}, Verde: {max_boxes - green_count}, Rosa: {max_boxes - pink_count}"
    text_surface = font.render(text, True, cuadro_color)
    screen.blit(text_surface, (margin, screen.get_height() - 2 * margin - text_surface.get_height()))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_t]:
        # Presionar la tecla "t" pausará o reanudará el juego
        pausado = not pausado
    if not pausado:
        if tiempo_restante == 0:
            texto_espera_turno = fuente_espera_turno.render(espera_turno_texto, True, (0, 0, 0))
            screen.blit(texto_espera_turno, (screen.get_width() - 200, 10))

        # Movemos el cuadrado con las teclas de flecha
        if key_input[pygame.K_UP] and rojoy > 0 and tiempo_restante <= 0:
            rojoy -= 4
        if key_input[pygame.K_DOWN] and rojoy + cubo_original.get_height() < rio.get_height() and tiempo_restante <= 0:
            rojoy += 4
        if key_input[pygame.K_LEFT] and rojox > 0 and tiempo_restante <= 0 and rojox>screen.get_width()/2:
            rojox -= 4
        if key_input[
            pygame.K_RIGHT] and rojox + cubo_original.get_width() < screen.get_width() and tiempo_restante <= 0 :
            rojox += 4

        # Movemos el punto con las teclas W, A, S y D
        if key_input[pygame.K_w] and point_y > 0 and point_y:
            point_y -= 4
        if key_input[pygame.K_s] and point_y < screen.get_height():
            point_y += 4
        if key_input[pygame.K_a] and point_x > 0 :
            point_x -= 4
        if key_input[pygame.K_d] and point_x < screen.get_width() and point_x<screen.get_width()/2:
            point_x += 4

        if key_input[pygame.K_l] and tiempo_restante <= 0:
            player_angle += 2

        if key_input[pygame.K_k] and tiempo_restante <= 0:
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
            # Si la tecla "q" se presiona y no está siendo mantenida presionada
            if not q_key_held:
                q_key_held = True
                if cuadro_color == BLUE and cubos_azules < 10:
                    nuevo_cuadro = {
                        'surface': cubo_original.copy(),
                        'x': point_x - cubo_original.get_width() / 2,
                        'y': point_y - cubo_original.get_height() / 2,
                        'color': cuadro_color  # Almacena el color actual
                    }
                    cuadrados.append(nuevo_cuadro)
                    cubos_azules += 1
                    print(cubos_azules)
                elif cuadro_color == GREEN and cubos_verdes < 10:
                    nuevo_cuadro = {
                        'surface': cubo_original.copy(),
                        'x': point_x - cubo_original.get_width() / 2,
                        'y': point_y - cubo_original.get_height() / 2,
                        'color': cuadro_color  # Almacena el color actual
                    }
                    cuadrados.append(nuevo_cuadro)
                    cubos_verdes += 1

                elif cuadro_color == PINK and cubos_rosados < 10:
                    nuevo_cuadro = {
                        'surface': cubo_original.copy(),
                        'x': point_x - cubo_original.get_width() / 2,
                        'y': point_y - cubo_original.get_height() / 2,
                        'color': cuadro_color  # Almacena el color actual
                    }
                    cuadrados.append(nuevo_cuadro)
                    cubos_rosados += 1
                elif cuadro_color == BROWN and aguila < 1:
                    nuevo_cuadro = {
                        'surface': cubo_original.copy(),
                        'x': point_x - cubo_original.get_width() / 2,
                        'y': point_y - cubo_original.get_height() / 2,
                        'color': cuadro_color  # Almacena el color actual
                    }
                    cuadrados.append(nuevo_cuadro)
                    aguila += 1
        else:
            # Restablecer el estado de la tecla "q" cuando se suelta
            q_key_held = False

        if key_input[pygame.K_1]:
            cuadro_color = BLUE  # Cambiar el color del cuadro a azul
            key_1_pressed = True
            key_2_pressed = False
            key_3_pressed = False
            key_4_pressed = False

        if key_input[pygame.K_2]:
            cuadro_color = GREEN  # Cambiar el color del cuadro a verde
            key_1_pressed = False
            key_2_pressed = True
            key_3_pressed = False
            key_4_pressed = False

        if key_input[pygame.K_3]:
            cuadro_color = PINK  # Cambiar el color del cuadro a rosa
            key_1_pressed = False
            key_2_pressed = False
            key_3_pressed = True
            key_4_pressed = False
        if key_input[pygame.K_4]:
            cuadro_color = BROWN  # Cambiar el color del cuadro a rosa
            key_1_pressed = False
            key_2_pressed = False
            key_3_pressed = False
            key_4_pressed = True

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
        texto_tiempo = fuente.render(f"haz tu estrategia: {tiempo_mostrar} s", True, (0,0,0))
        screen.blit(texto_tiempo, (10, 10))

        draw_color_boxes(screen, max_cubos_por_color, cubos_azules, cubos_verdes, cubos_rosados, aguila)





    else:
        # Si está en pausa, muestra un aviso en la pantalla
        pygame.draw.rect(screen, pausa_text_color, (pausa_text_x, pausa_text_y, pausa_text_width, pausa_text_height))
        fuente_pausa = pygame.font.Font(None, 24)
        texto_pausa = fuente_pausa.render("Juego pausado", True, WHITE)
        screen.blit(texto_pausa, (pausa_text_x + 10, pausa_text_y + 5))




    pygame.display.update()
    clock.tick(144)