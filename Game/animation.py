import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((1024,720))
pygame.display.set_caption("Example")

background = pygame.image.load("Scenary/Arena Tileset Template Verde.png")

#GoblinSprite = pygame.image.load("Goblin King Sprite .png")
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
GoblinRect.center = (400,300)
GoblinSpeed = 1.3

GoblinLeft = False
GoblinRight = False

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
    now = pygame.time.get_ticks()

    if GoblinMovin:
          if now -lastUpdate > GoblinAnimationSpeed * 1000:
                lastUpdate = now
                CurrentFrame = (CurrentFrame+1)%len(GoblinWalk)

    if now - lastUpdate > GoblinAnimationSpeed * 1000:  # Convierte a milisegundos
        lastUpdate = now
        CurrentFrame = (CurrentFrame + 1) % len(GoblinWalk)

    keys = pygame.key.get_pressed()

    
    if any(keys):
        GoblinMovin = False
        GoblinLeft = False
        GoblinRight = False
          
    if keys[pygame.K_LEFT]:
                GoblinRect.x -= GoblinSpeed
                GoblinMovin = True
                GoblinLeft = True
    if keys[pygame.K_RIGHT]:
                GoblinRect.x += GoblinSpeed
                GoblinMovin = True
                GoblinRight = True
    if keys[pygame.K_UP]:
                GoblinRect.y -= GoblinSpeed
                GoblinMovin = True
    if keys[pygame.K_DOWN]:
                GoblinRect.y += GoblinSpeed
                GoblinMovin = True
 
    
          
    # Limpia la pantalla
    #screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

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
        
    

    # Actualiza la pantalla
    pygame.display.update()
    clock.tick(60)
