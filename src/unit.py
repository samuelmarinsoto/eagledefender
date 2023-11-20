import unittest
import pygame
import users
from disparoclase import Bala

class testjuego(unittest.TestCase):

    def test_bloques(self):
        pygame.init()
        pantalla = pygame.display.set_mode((500, 500))

        pared = Bala(0, 'A', pantalla, 0, 0, 0)
        self.assertEqual(pared.vida, 3)
        self.assertEqual(pared.posx, 0)
        self.assertEqual(pared.posy, 0)
        self.assertEqual(pared.angulo, 0)
        self.assertEqual(pared.rol, 0)
        self.assertEqual(pared.tipo, 'A')
        self.assertEqual(pared.pantalla, pantalla)

        pared2 = Bala(1, 'B', pantalla, 200, 200, 90)
        self.assertEqual(pared2.vida, 5)
        self.assertEqual(pared2.posx, 200)
        self.assertEqual(pared2.posy, 200)
        self.assertEqual(pared2.angulo, 90)
        self.assertEqual(pared2.rol, 1)
        self.assertEqual(pared2.tipo, 'B')
        self.assertEqual(pared2.pantalla, pantalla)

        
        
