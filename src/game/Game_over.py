import pygame
import sys

class GameWindow:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Ventana del Juego")
        self.running = True

    def mostrar_ganador(self, ganador):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((255, 255, 255))
            font = pygame.font.Font(None, 36)
            text = font.render(f"Ganador: {ganador}", True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            self.window.blit(text, text_rect)
            pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()
        sys.exit()