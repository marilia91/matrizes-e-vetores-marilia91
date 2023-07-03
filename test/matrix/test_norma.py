"""Esse arquivo testa o arquivo matrix.py"""

import unittest

from matrix import norma
from tipos import Matriz


class TestMatrixNorma(unittest.TestCase):
    """Classe para testar a função norma no arquivo matrix.py"""

    def test_norma_vazia(self):
        """Testa se a resposta é zero para matrizes vazias"""
        self.assertEqual(norma([]), 0)

    def test_norma_1x1(self):
        """Testa se a norma da matriz [[1]] é 1 e da matriz [[-1]] é 1"""
        x: Matriz = [[1]]
        self.assertEqual(norma(x), 1)
        y: Matriz = [[-1]]
        self.assertEqual(norma(y), 1)

    def test_norma_2x2(self):
        """
        Testa se a norma da matriz [[1, 2], [2, 3]] é 4.2426406871193
        e da matriz [[-1, 2], [2, -3]] é 4.2426406871193
        """
        x: Matriz = [[1, 2], [2, 3]]
        self.assertAlmostEqual(norma(x), 4.2426406871193, delta=0.01)
        y: Matriz = [[-1, 2], [2, -3]]
        self.assertAlmostEqual(norma(y), 4.2426406871193, delta=0.01)
