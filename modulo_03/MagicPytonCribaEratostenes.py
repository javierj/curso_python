import unittest
from unittest.mock import MagicMock

class CribaEratostenes:
	def calcula(self, val):
		#lb = None
		lb =  self.creaListaDeNumerosSinMarcar(val)
		self.marcarMultiplos(lb)
		return self.creaListaDePrimos(lb)


class TestBase(unittest.TestCase):

	def test_richtSequenceOfCalls(self):
		criba = CribaEratostenes()

		criba.creaListaDeNumerosSinMarcar = MagicMock(return_value=None)
		criba.marcarMultiplos = MagicMock() 
		criba.creaListaDePrimos = MagicMock()

		criba.calcula(5)

		criba.creaListaDeNumerosSinMarcar.assert_called_once_with(5)
		criba.marcarMultiplos.assert_called_once_with(None)
		criba.creaListaDePrimos.assert_called_once_with(None)


# Main
if __name__ == '__main__':
    unittest.main()

