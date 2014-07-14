__author__ = 'Javier'

import unittest
from itertools import cycle


class TestCycle(unittest.TestCase):

    def test_cycle_returns_next_element_in_the_iterator(self):
        cycle_list = cycle([1, 2, 3])
        self.assertEqual(1, cycle_list.__next__())
        self.assertEqual(2, cycle_list.__next__())
        self.assertEqual(3, cycle_list.__next__())

    def test_when_cycle_arrives_to_the_end_it_repeats_elements_in_same_order(self):
        cycle_list = cycle([1, 2])
        self.assertEqual(1, cycle_list.__next__())
        self.assertEqual(2, cycle_list.__next__())
        self.assertEqual(1, cycle_list.__next__())
        self.assertEqual(2, cycle_list.__next__())

    def test_cycle_supports_any_iterable_parameter(self):
        cycle_string = cycle("abc")
        self.assertEqual("a", cycle_string.__next__())
        self.assertEqual("b", cycle_string.__next__())
        cycle_tuple = cycle((1, 2))
        self.assertEqual(1, cycle_tuple.__next__())
        self.assertEqual(2, cycle_tuple.__next__())
        cycle_dict = cycle({1: "a", 2: "b"})
        self.assertEqual(1, cycle_dict.__next__())
        self.assertEqual(2, cycle_dict.__next__())

    # Tip: ¿Cómo podemos escribir esta prueba de una manera más sencilla con lo que nos ofrece UnitTest?
    def test_not_support_non_iterables_parameters(self):
        try:
            cycle_integer = cycle(1)
            self.fail("No exception")
        except TypeError:
            return
        self.fail("No valid exception")


if __name__ == '__main__':
    unittest.main()
