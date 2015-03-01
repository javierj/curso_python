__author__ = 'Javier'

import unittest


class TestFizzbuzzWithGen(unittest.TestCase):

    def _match_filters(self, value, filters):
        returned = ""
        for key, val in filters.items():
            if value % key == 0:
                returned += val
        return returned


    def fizzbuzz(self, limit):
        filters = {3: 'fizz', 5:'buzz'}
        source = 1
        while source <= limit:
            returned = self._match_filters(source, filters)
            if returned == "":
                returned = str(source)
            yield returned
            source +=1

    def fizzbuzz_aslist(self, limit):
        return list(self.fizzbuzz(limit))


    def test_fizzbuzz_1(self):
        self.assertEqual(['1'], self.fizzbuzz_aslist(1))
        self.assertEqual(['1', '2'], self.fizzbuzz_aslist(2))

    def test_fizzs(self):
        result = self.fizzbuzz_aslist(6)
        self.assertEqual(result[2], 'fizz')
        self.assertEqual(result[5], 'fizz')

    def test_buzzs(self):
        result = self.fizzbuzz_aslist(11)
        self.assertEqual(result[4], 'buzz')
        self.assertEqual(result[9], 'buzz')

    def test_fizzbuzzs(self):
        result = self.fizzbuzz_aslist(16)
        self.assertEqual(result[14], 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()
