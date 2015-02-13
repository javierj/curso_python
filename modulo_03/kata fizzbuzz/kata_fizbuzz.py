__author__ = 'Javier'

"""

1, 2, fizz, 4, buzz, fizz, 7, 8, fizz,....., fizzbuzz

0 -> []
1 -> [1]
2 -> [1, 2]
3 -> [1, 2, Fizz]

Escribir prueba y ver que falla -> Escribir mínimo código y ver que TODAS las pruebas pasan -> Refactorizar
Babystep

"""

import unittest


class Fizz_buzz(object):

    def _filtro(self, num, val, cad):
        if num % val == 0:
            return cad
        return ""

    def _filtro_si_3(self, num):
        return self._filtro(num, 3, "fizz")

    def fizzbuzz(self, limit_val):
        fizzbuzz_list = list()
        for num in range(1, limit_val +1):
            next_elem= ""
            next_elem += self._filtro_si_3(num)
            next_elem += self._filtro(num, 5, "buzz")
            if next_elem is "":
                next_elem= str(num)
            fizzbuzz_list.append(next_elem)
        return fizzbuzz_list


class FactoryFizzBuzz(object):

    def fizzbuzz(self, limit_val):
        return Fizz_buzz().fizzbuzz(limit_val)


class TestFizzBuzz(unittest.TestCase):

    def fizzbuzz(self, limit_val):
        return Fizz_buzz().fizzbuzz(limit_val)

    def test_empty_fizzbuzz(self):
        result = self.fizzbuzz(0)
        self.assertEqual(len(result), 0)

    def test_first_numer(self):
        result = self.fizzbuzz(2)
        self.assertEqual(result, ['1', '2'])

    def test_fizz(self):
        result = self.fizzbuzz(6)
        self.assertEqual('fizz', result[2])
        self.assertEqual('fizz', result[5])

    def test_buzz(self):
        result = self.fizzbuzz(5)
        self.assertEqual('buzz', result[4])

    def test_multiplo_3_y_5_a_la_vez(self):
        result = self.fizzbuzz(15)
        self.assertEqual('fizzbuzz', result[14])


if __name__ == '__main__':
    unittest.main()
