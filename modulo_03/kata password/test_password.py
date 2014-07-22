__author__ = 'Javier'

import unittest
import verify_password


class MyTestCase(unittest.TestCase):

    def test_password_menos_6_caracteres_es_incorrecto(self):
        self.assertFalse(self.is_valid("abc_0"))

    def test_password_correcto(self):
        self.assertTrue(self.is_valid("abc_01"))
        self.assertTrue(self.is_valid("ABC_01"))

    def test_password_sin_guionbajo_es_incorrecto(self):
        self.assertFalse(self.is_valid("abc012"))

    def test_password_sin_numeros_es_incorrecto(self):
        self.assertFalse(self.is_valid("abc_ef"))

    def test_password_sin_letras_es_incorrecto(self):
        self.assertFalse(self.is_valid("123_456"))


    def is_valid(self, password):
        return verify_password.verify(password)

if __name__ == '__main__':
    unittest.main()
