import pygame

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w/2,pygame.display.Info().current_h/2))
pygame.display.set_caption('Eagle Defender')
clock = pygame.time.Clock()

rio = pygame.Surface((20,pygame.display.get_surface().get_height()))
rio.fill('Blue')

cubo_rojo = pygame.Surface((50,50))
cubo_rojo.fill('Red')


rojox = 150
rojoy = 300
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
                     
    clock.tick(144)
    screen.fill((0,0,0))
    screen.blit(rio,((pygame.display.get_surface().get_width()//2)-10,0))
    screen.blit(cubo_rojo,(rojox,rojoy))
    pygame.display.update()
