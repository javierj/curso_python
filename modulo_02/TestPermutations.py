__author__ = 'Javier'

import unittest
from itertools import permutations


class MyTestCase(unittest.TestCase):

    def countInIterator(self, iterator):
        count = 0
        for _ in iterator:
            count += 1
        return count

    def test_permutaciones_correcto(self):
        # Arrange

        # Act
        resultado = self.crear_permutaciones([1, 2])

        # Assert
        #self.assertEqual(resultado.__next__(), (1,2))
        #self.assertEqual(resultado.__next__(), (2,1))
        #self.assertEqual(self.countInIterator(resultado), 2)
        self.assertEqual(len(resultado), 2)
        self.assertIn((1,2), resultado)
        self.assertIn((2,1), resultado)

        resultado = permutations([1, 2, 3])

        # Assert
        self.assertEqual(resultado.__next__(), (1,2, 3))
        self.assertEqual(resultado.__next__(), (1, 3, 2))
        self.assertEqual(resultado.__next__(), (2, 1, 3))
        self.assertEqual(resultado.__next__(), (2, 3, 1))


    def test_permutaciones_con_parametro(self):
        resultado = self.crear_permutaciones([1, 2], 1)

        self.assertEqual(len(resultado), 2)
        self.assertIn((1,), resultado)
        self.assertIn((2,), resultado)

        resultado = self.crear_permutaciones([1, 2, 3], 2)
        self.assertEqual(len(resultado), 6)


    def test_lista_vacia(self):
        resultado = self.crear_permutaciones([])
        self.assertEqual(len(resultado), 1)
        self.assertIn(tuple(), resultado)


    def test_cero_elementos(self):
        resultado = self.crear_permutaciones([1, 2], 0)

        self.assertEqual(len(resultado), 1)
        self.assertIn(tuple(), resultado)


    def test_parametro_negativo(self):
        def crear_permutaciones_con_excepcion():
            self.crear_permutaciones([1, 2], -1)

        self.assertRaises(ValueError, crear_permutaciones_con_excepcion)
        self.assertRaises(ValueError, lambda : self.crear_permutaciones([1, 2], -1))


    def test_iterables(self):
        resultado = self.crear_permutaciones({1:"a", 2:"b"})

        self.assertEqual(len(resultado), 2)
        self.assertIn((1,2), resultado)

        resultado = self.crear_permutaciones((1,2))

        self.assertEqual(len(resultado), 2)
        self.assertIn((1,2), resultado)
        self.assertIn((2, 1), resultado)

        resultado = self.crear_permutaciones("ab")

        self.assertEqual(len(resultado), 2)
        self.assertIn(("a","b"), resultado)
        self.assertIn(("b", "a"), resultado)







    def crear_permutaciones(self, elementos, tamanyo = None):
        if tamanyo is None:
            tamanyo = len(elementos)
        return list(permutations(elementos, tamanyo))


if __name__ == '__main__':
    unittest.main()
