__author__ = 'Javier'

import unittest
from itertools import cycle


class TestCycle(unittest.TestCase):

    def setUp(self):
        self.cuadrados = [x*x for x in range(5)]

    def tearDown(self):
        print("Fin de la prueba.")

    def test_tipo_de_cuadrados(self):
        self.assertIsNotNone(self.cuadrados)
        self.assertIsInstance(self.cuadrados, list)

    def test_numero_de_elementos_en_cuadrados(self):
        self.assertEqual(len(self.cuadrados), 5)

    def test_elementos_en_la_lusa(self):
        self.assertIn(0, self.cuadrados)
        self.assertIn(4, self.cuadrados)

    def test_contenido_de_la_lista(self):
        self.assertListEqual(self.cuadrados, [0, 1, 4, 9, 16])

    def test_falla_al_acceder_a_un_elemento_que_no_existe(self):
        def get_quinto_elemento():
            return self.cuadrados[5]
        self.assertRaises(IndexError, get_quinto_elemento)