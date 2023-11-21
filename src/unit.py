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

    def test_poderes(self):
        pygame.init()
        pantalla = pygame.display.set_mode((500, 500))
        
        bala = Bala(0, 'A', pantalla, 0, 0, 0)
        self.assertEqual(bala.vida, 3)
        self.assertEqual(bala.posx, 0)
        self.assertEqual(bala.posy, 0)
        self.assertEqual(bala.angulo, 0)
        self.assertEqual(bala.rol, 0)
        self.assertEqual(bala.tipo, 'A')
        self.assertEqual(bala.pantalla, pantalla)

        bala.moverse(1)
        self.assertEqual(bala.posx, 700)
        self.assertEqual(bala.posy, 0)

        bala2 = Bala(1, 'B', pantalla, 200, 200, 90)
        self.assertEqual(bala2.vida, 5)
        self.assertEqual(bala2.posx, 200)
        self.assertEqual(bala2.posy, 200)
        self.assertEqual(bala2.angulo, 90)
        self.assertEqual(bala2.rol, 1)
        self.assertEqual(bala2.tipo, 'B')
        self.assertEqual(bala2.pantalla, pantalla)

        bala2.moverse(1)
        self.assertEqual(bala2.posx, 200.00000000000006)
        self.assertEqual(bala2.posy, 900)
        
