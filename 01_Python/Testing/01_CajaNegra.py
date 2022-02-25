# Esta son pruebas para verificar que, dados unos inputs,
# obtenemos los outputs que esperamos.
# Todos los métodos que defina como casos de prueba
# deben comenzar con la palabra "test"

import unittest


def suma(num_1, num_2):
    return num_1 + num_2
    # return abs(num_1) + num_2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()