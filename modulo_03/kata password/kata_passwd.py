__author__ = 'Javier'


"""

Validador de claves

- Mínimo 6 caracteres
- Mínimo un número
- Mínimo una mayúscula
- El caracter _

"" -> False porque la sincumple todas
"12345" -> False no tiene 6 caracteres, no iene mayúsuca, no tiene _
"A123456_" -> True
"abc_1de" -> No tiene mayúscula
"..." ->

"""

import unittest
import re


def _chek_if_not_match(pattern, string):
    return re.search(pattern, string) == None

def validar_passwd(passwd):
    if _chek_if_not_match("[A-Z]", passwd):
        return False
    if _chek_if_not_match("[0-9]", passwd):
        return False
    if not "_" in passwd:
        return False
    if len(passwd) < 6:
        return False
    return True


class MyTestCase(unittest.TestCase):

    def validar_passwd(self, passwd):
        return validar_passwd(passwd)

    def test_cadena_correcta(self):
        self.assertTrue(self.validar_passwd("A123456_"))

    def test_falta_mayuscula(self):
        self.assertFalse(self.validar_passwd("abc_1de"))

    def test_falta_numero(self):
        self.assertFalse(self.validar_passwd("Abc_xde"))

    def test_falta_guion_bajo(self):
        self.assertFalse(self.validar_passwd("Abc1xde"))

    def test_menos_de_6_caracteres(self):
        self.assertFalse(self.validar_passwd("A1_bd"))

    def test_cadena_vacia(self):
        self.assertFalse(self.validar_passwd(""))

if __name__ == '__main__':
    unittest.main()
