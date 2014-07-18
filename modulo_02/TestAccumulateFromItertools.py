__author__ = 'Javier'

import unittest
from itertools import accumulate
#import sure



class TestAccumulate(unittest.TestCase):

    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    def test_main_function(self):
        #lista1 = []
        lista2 = list(accumulate([1,2,3,4,5]))
        #lista3 = [x for x in accumulate([1,2,3,4,5])]
        self.assertListEqual(lista2, [1,3,6,10,15])
        #self.assertListEqual(lista3, [1,3,6,10,15])

    def test_es_vacia(self):
        lista_vacia = list(accumulate([]))
        self.assertListEqual(lista_vacia, [])
        #lista_vacia.should.be.empty;

    @staticmethod
    def resta2(a, b):
        return b-a

    def test_(self):
        def resta(a, b):
            return b-a
        lista = list(accumulate([1, 1, 1], lambda a, b: b-a))
        self.assertListEqual(lista, [1, 0, 1])

if __name__ == '__main__':
    unittest.main()
