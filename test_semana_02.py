import unittest
from semana_02 import *


class TestPropagarFunction(unittest.TestCase):

    def test_example_1(self): # Visto en clase
        fos = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
        resultado_esperado = [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
        self.assertEqual(propagar(fos), resultado_esperado)

    def test_example_2(self): # Visto en clase
        fos = [0, 0, 0, 1, 0, 0]
        resultado_esperado = [1, 1, 1, 1, 1, 1]
        self.assertEqual(propagar(fos), resultado_esperado)

    def test_example_3(self):
        fos = [0, 0, 0, 0, 0]
        resultado_esperado = [0, 0, 0, 0, 0]  # Debería devolver todos 0
        self.assertEqual(propagar(fos), resultado_esperado)


class TestInvertirLista(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(invertir_lista([]), [])

    def test_example_2(self):
        self.assertEqual(invertir_lista([1, 2, 3]), [3, 2, 1])

    def test_example_3(self):
        self.assertEqual(invertir_lista(['a', 'b', 'c']), ['c', 'b', 'a'])

    def test_example_4(self):
        self.assertEqual(invertir_lista([1, 'a', 3.5]), [3.5, 'a', 1])


class TestCollatz(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(collatz(6), 8)
    
    def test_example_2(self):
        with self.assertRaises(AssertionError):
            collatz(0)

    def test_example_3(self):
        with self.assertRaises(AssertionError):
            collatz(-1)

class TestContarDefiniciones(unittest.TestCase):
    def test_example_1(self):
        my_dict = {'a': [1, 2], 'b': [3], 'c': []}
        resultado_esperado = {'a': 2, 'b': 1, 'c': 0}
        self.assertEqual(contar_definiciones(my_dict), resultado_esperado)

    def test_example_2(self):
        my_dict = {}
        resultado_esperado = {}
        self.assertEqual(contar_definiciones(my_dict), resultado_esperado)


class TestCantidadDeClavesLetra(unittest.TestCase):
    def test_example_1(self):
        my_dict = {'river': 1, 'boca': 2, 'bandield': 3}
        start = 'b'
        resultado_esperado = 2
        self.assertEqual(cantidad_de_claves_letra(my_dict, start), resultado_esperado)

    def test_example_2(self):
        my_dict = {'river': 1, 'boca': 2, 'independiente': 3}
        start = 'b'
        resultado_esperado = 1
        self.assertEqual(cantidad_de_claves_letra(my_dict, start), resultado_esperado)

if __name__ == '__main__':
    unittest.main()