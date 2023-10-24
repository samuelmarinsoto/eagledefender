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

GoblinWalk = [pygame.image.load("goblinSpriteWalk/tile000.png"),
              pygame.image.load("goblinSpriteWalk/tile001.png"),
              pygame.image.load("goblinSpriteWalk/tile002.png"),
              pygame.image.load("goblinSpriteWalk/tile003.png"),
              pygame.image.load("goblinSpriteWalk/tile004.png"),
              pygame.image.load("goblinSpriteWalk/tile005.png")]

GoblinStatic = pygame.image.load("goblinSpriteWalk/tile100.png")
GoblinMovin = False

GoblinAnimationSpeed = 0.2
CurrentFrame = 0
lastUpdate = pygame.time.get_ticks()

GoblinRect = GoblinWalk[0].get_rect()
GoblinRect.center = (750,300)
GoblinSpeed = 1.3

GoblinLeft = False
GoblinRight = False

cubo_original = pygame.Surface((50, 50))
cubo_original.fill('Blue')
cubo_rojo = cubo_original.copy()

bola = pygame.Surface((10, 10))
bola.fill('Green')

rojox = 750
rojoy = 300
player_angle = 0
bullet = None
bullet_speed = 7

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

# texturas

textura_madera = pygame.image.load("assets/bloquemadera.png")
textura_madera = pygame.transform.scale(textura_madera, (screen.get_height()//20, screen.get_height()//20))
textura_acero = pygame.image.load("assets/bloquemetal.png")
textura_acero = pygame.transform.scale(textura_acero, (screen.get_height()//20, screen.get_height()//20))
textura_concreto = pygame.image.load("assets/bloqueconcreto.png")
textura_concreto = pygame.transform.scale(textura_concreto, (screen.get_height()//20, screen.get_height()//20))


background = pygame.image.load("Scenary/Arena Tileset Template Verde.png")
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))


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


def draw_color_boxes(screen, max_boxes, madera_count, acero_count, concreto_count, seleccion):
    box_size = 30
    margin = 10
    box_x = margin
    box_y = screen.get_height() - (max_boxes * (box_size + margin) + margin)

    # Dibujar cuadros de colores

    # Mostrar el texto indicador
    font = pygame.font.Font(None, 24)
    textmadera = f"Madera: {max_boxes - madera_count}"
    textacero = f"Acero: {max_boxes - acero_count}"
    textconcreto = f"Concreto: {max_boxes - concreto_count}"
    if seleccion == BLUE:
        madera_textsurf = font.render(textmadera, True, (255,0,0))
    else:
        madera_textsurf = font.render(textmadera, True, (0,0,0))
        
    if seleccion == GREEN:
        acero_textsurf = font.render(textacero, True, (255,0,0))
    else:
        acero_textsurf = font.render(textacero, True, (0,0,0))
        
    if seleccion == PINK:
        concreto_textsurf = font.render(textconcreto, True, (255,0,0))
    else:
        concreto_textsurf = font.render(textconcreto, True, (0,0,0))
    
    screen.blit(madera_textsurf, (margin, screen.get_height() - 2 * margin - madera_textsurf.get_height() -100 ))
    screen.blit(acero_textsurf, (margin, screen.get_height() - 2 * margin - acero_textsurf.get_height() -50 ))
    screen.blit(concreto_textsurf, (margin, screen.get_height() - 2 * margin - concreto_textsurf.get_height()))


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

        now = pygame.time.get_ticks()

        if GoblinMovin:
            if now -lastUpdate > GoblinAnimationSpeed * 1000:
                lastUpdate = now
                CurrentFrame = (CurrentFrame+1)%len(GoblinWalk)

        if now - lastUpdate > GoblinAnimationSpeed * 1000:  # Convierte a milisegundos
            lastUpdate = now
            CurrentFrame = (CurrentFrame + 1) % len(GoblinWalk)

        

    
        if any(key_input):
            GoblinMovin = False
            GoblinLeft = False
            GoblinRight = False
          
        if key_input[pygame.K_LEFT]:
                    GoblinRect.x -= GoblinSpeed
                    GoblinMovin = True
                    GoblinLeft = True
        if key_input[pygame.K_RIGHT]:
                    GoblinRect.x += GoblinSpeed
                    GoblinMovin = True
                    GoblinRight = True
        if key_input[pygame.K_UP]:
                    GoblinRect.y -= GoblinSpeed
                    GoblinMovin = True
        if key_input[pygame.K_DOWN]:
                    GoblinRect.y += GoblinSpeed
                    GoblinMovin = True

        
        """
        if key_input[pygame.K_UP] and rojoy > 0 and tiempo_restante <= 0:
            rojoy -= 4
        if key_input[pygame.K_DOWN] and rojoy + cubo_original.get_height() < rio.get_height() and tiempo_restante <= 0:
            rojoy += 4
        if key_input[pygame.K_LEFT] and rojox > 0 and tiempo_restante <= 0 and rojox>screen.get_width()/2:
            rojox -= 4
        if key_input[
            pygame.K_RIGHT] and rojox + cubo_original.get_width() < screen.get_width() and tiempo_restante <= 0 :
            rojox += 4"""

        # Movemos el punto con las teclas W, A, S y D
        if key_input[pygame.K_w] and point_y > 0 and point_y:
            point_y -= 7
        if key_input[pygame.K_s] and point_y < screen.get_height():
            point_y += 7
        if key_input[pygame.K_a] and point_x > 0 :
            point_x -= 7
        if key_input[pygame.K_d] and point_x < screen.get_width() and point_x<screen.get_width()/2:
            point_x += 7

        if key_input[pygame.K_l] and tiempo_restante <= 0:
            player_angle += 6
        
        if key_input[pygame.K_o] and tiempo_restante <= 0:
            player_angle -= 6

        if key_input[pygame.K_k] and tiempo_restante <= 0:
            if bullet is None:
                bullet = {
                    'x': GoblinRect.x + cubo_original.get_width() / 2,
                    'y': GoblinRect.y + cubo_original.get_height() / 2,
                    'dx': bullet_speed * math.cos(math.radians(player_angle)),
                    'dy': -bullet_speed * math.sin(math.radians(player_angle)),
                    'color': GREEN  # Cambia el color de la bola a verde
                }

        if key_input[pygame.K_j]:
            if bullet is None:
                bullet = {
                    'x': GoblinRect.x + cubo_original.get_width() / 2,
                    'y': GoblinRect.y + cubo_original.get_height() / 2,
                    'dx': bullet_speed * math.cos(math.radians(player_angle)),
                    'dy': -bullet_speed * math.sin(math.radians(player_angle)),
                    'color': BLUE  # Cambia el color de la bola a azul
                }

        if key_input[pygame.K_h]:
            if bullet is None:
                bullet = {
                    'x': GoblinRect.x + cubo_original.get_width() / 2,
                    'y': GoblinRect.y + cubo_original.get_height() / 2,
                    'dx': bullet_speed * math.cos(math.radians(player_angle)),
                    'dy': -bullet_speed * math.sin(math.radians(player_angle)),
                    'color': RED  # Cambia el color de la bola a rojo
                }

        screen.blit(background,(0,0))
       
        player_x = GoblinRect.x + cubo_original.get_width() / 2
        player_y = GoblinRect.y + 40 + cubo_original.get_height() / 2
        rotated_cubo = pygame.transform.rotate(cubo_original, player_angle)
        player_rect = rotated_cubo.get_rect(center=(player_x, player_y))

        # screen.fill((255, 255, 255))
        # screen.blit(rio, ((pygame.display.get_surface().get_width() // 2) - 10, 0))

        # Dibujar una línea más grande que indica la dirección del frente del cuadrado
        front_x = player_x + line_length * math.cos(math.radians(player_angle))
        front_y = player_y - line_length * math.sin(math.radians(player_angle))
        pygame.draw.line(screen, (255, 0, 0), (player_x, player_y), (front_x, front_y), line_width)

        # Utilizamos el cuadro original sin cambios de tamaño
        #screen.blit(rotated_cubo, player_rect.topleft)

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
            # cuadrado_surface.fill(cuadrado['color'])  # Usar el color almacenado en la estructura
            screen.blit(cuadrado_surface, (cuadrado['x'], cuadrado['y']))

        if key_input[pygame.K_q]:
            # Si la tecla "q" se presiona y no está siendo mantenida presionada
            if not q_key_held:
                q_key_held = True
                if cuadro_color == BLUE and cubos_azules < 10:
                    nuevo_cuadro = {
                        'surface': textura_madera,
                        'x': point_x - cubo_original.get_width() / 2,
                        'y': point_y - cubo_original.get_height() / 2,
                        'color': cuadro_color  # Almacena el color actual
                    }
                    cuadrados.append(nuevo_cuadro)
                    cubos_azules += 1
                    print(cubos_azules)
                elif cuadro_color == GREEN and cubos_verdes < 10:
                    nuevo_cuadro = {
                        'surface': textura_acero,
                        'x': point_x - cubo_original.get_width() / 2,
                        'y': point_y - cubo_original.get_height() / 2,
                        'color': cuadro_color  # Almacena el color actual
                    }
                    cuadrados.append(nuevo_cuadro)
                    cubos_verdes += 1

                elif cuadro_color == PINK and cubos_rosados < 10:
                    nuevo_cuadro = {
                        'surface': textura_concreto,
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
                
       
        if GoblinMovin:
            GoblinMovin = False
            if GoblinLeft:
                    screen.blit(pygame.transform.flip(GoblinWalk[CurrentFrame],True,False), GoblinRect)
            elif GoblinRight:
                    screen.blit(GoblinWalk[CurrentFrame], GoblinRect)
            else:
                    screen.blit(GoblinWalk[CurrentFrame], GoblinRect)
        else:
            screen.blit(GoblinStatic,GoblinRect)


        
        # ...

        # Mostrar el tiempo restante en la pantalla
        tiempo_mostrar = tiempo_restante // 1000  # Convertir a segundos
        texto_tiempo = fuente.render(f"haz tu estrategia: {tiempo_mostrar} s", True, (0,0,0))
        screen.blit(texto_tiempo, (10, 10))

        draw_color_boxes(screen, max_cubos_por_color, cubos_azules, cubos_verdes, cubos_rosados, cuadro_color)

      



    else:
        # Si está en pausa, muestra un aviso en la pantalla
        pygame.draw.rect(screen, pausa_text_color, (pausa_text_x, pausa_text_y, pausa_text_width, pausa_text_height))
        fuente_pausa = pygame.font.Font(None, 24)
        texto_pausa = fuente_pausa.render("Juego pausado ", True, WHITE)
        screen.blit(texto_pausa, (pausa_text_x + 10, pausa_text_y + 5))


    

    pygame.display.update()
    clock.tick(60)
