import unittest
import pygame
import datauser


class testdatauser(unittest.TestCase):

    def test_datauser(self):
        self.assertEqual(datauser.validar_tarjeta("1234567890123456", "12/25", "123", "Juan Perez"), (True, "Tarjeta válida"))
        self.assertEqual(datauser.validar_tarjeta("2313212133123336", "11/25", "193", "Jose Pereira"), (True, "Tarjeta válida"))

        self.assertEqual(datauser.validar_tarjeta("1234567856", "12/25", "123", "Juan Perez"), (False,"Número de tarjeta inválido"))
        self.assertEqual(datauser.validar_tarjeta("1234567890123456", "12/20", "123", "Juan Perez"), (False,"Tarjeta vencida"))
        self.assertEqual(datauser.validar_tarjeta("1234567890123456", "12/25", "12", "Juan Perez"), (False,"Código de seguridad inválido"))
        self.assertEqual(datauser.validar_tarjeta("1234567890123456", "12/25", "123", "Juan Perez1"), (False,"Nombre del titular inválido"))

        self.assertEqual(datauser.LastNameCheck("Perez"), "Perez")
        self.assertEqual(datauser.LastNameCheck("Perez1"), "Perez1")
        self.assertEqual(datauser.LastNameCheck(123), 0)

        self.assertEqual(datauser.FirstNameCheck("Juan"), "Juan")
        self.assertEqual(datauser.FirstNameCheck("Juan1"), "Juan1")
        self.assertEqual(datauser.FirstNameCheck(123), 0)

        self.assertEqual(datauser.validar_usuario("Juan"), (False,"El usuario debe ser mayor 8 caracteres y menor que 16"))
        self.assertEqual(datauser.validar_usuario("Juan123456789"), (True,""))
        self.assertEqual(datauser.validar_usuario("Juan1234567891213"), (False,"El usuario debe ser mayor 8 caracteres y menor que 16"))
        self.assertEqual(datauser.validar_usuario(123), False)
        self.assertEqual(datauser.validar_usuario("ceja2013"), (False,"Usuario en uso"))
        self.assertEqual(datauser.validar_usuario("CejasCaca12"), (False,"Palabra inapropiada: "+ "caca"))

        self.assertEqual(datauser.validar_contrasena("Juan123456789"), True)
        self.assertEqual(datauser.validar_contrasena("Juan1234567891213"), False)
        self.assertEqual(datauser.validar_contrasena(123), False)
        self.assertEqual(datauser.validar_contrasena("ceja2013"), False)
        self.assertEqual(datauser.validar_contrasena("CejasCaca12"), True)

        self.assertEqual(datauser.MailCheck("fabianzona@gmail.com"), "fabianzona@gmail.com")
        self.assertEqual(datauser.MailCheck("fabianzona@gmail"), (0,"Dominio no válido"))
        self.assertEqual(datauser.MailCheck("fabianzona.com"), (0,"Falta @ en el correo"))
        self.assertEqual(datauser.MailCheck("fabianzona"), (0,"Falta @ en el correo"))
        self.assertEqual(datauser.MailCheck(123), (0,"Correo no válido"))







