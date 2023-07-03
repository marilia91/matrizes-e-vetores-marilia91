"""Esse arquivo testa o arquivo vector.py"""

import unittest

from tipos import Vetor
from vector import norma


class TestVectorNorma(unittest.TestCase):
    """Classe para testar a função norma no arquivo vector.py"""

    def test_norma_vazia(self):
        """Testa se a resposta é None para vetores vazios"""
        self.assertEqual(norma([]), None)

    def test_norma_1(self):
        """Testa se a resposta é correta para o vetor [1]"""
        x: Vetor = [1]
        self.assertEqual(norma(x), 1)

    def test_norma_2(self):
        """Testa se a resposta é correta para o vetor [1, 2]"""
        x: Vetor = [1, 2]
        resultado = norma(x)
        if resultado is not None:
            self.assertAlmostEqual(resultado, 5**0.5, delta=0.01)
        else:
            self.fail("Resultado não deveria ser None")

    def test_norma_3(self):
        """Testa se a resposta é correta para o vetor [1, 2, 3]"""
        x: Vetor = [1, 2, 3]
        resultado = norma(x)
        if resultado is not None:
            self.assertAlmostEqual(resultado, 14**0.5, delta=0.01)
        else:
            self.fail("Resultado não deveria ser None")
