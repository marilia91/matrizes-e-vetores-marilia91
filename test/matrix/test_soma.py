"""Esse arquivo testa o arquivo matrix.py"""

import unittest  # for creating the test case

from matrix import soma
from tipos import Matriz


class TestMatrixSoma(unittest.TestCase):
    """Classe para testar a função soma no arquivo matrix.py"""

    def test_soma_vazia(self):
        """Testa se a resposta é vazia para matrizes vazias"""
        self.assertEqual(soma([], []), [])

    def test_soma_impossivel(self):
        """Testa se a resposta é None para matrizes incompatíveis"""
        x: Matriz = [[1]]
        y: Matriz = []
        self.assertEqual(soma(x, y), None)

    def test_soma_1x1(self):
        """Testa se a soma das matrizes [[1]] e [[2]] é [[3]]"""
        x: Matriz = [[1]]
        y: Matriz = [[2]]
        self.assertEqual(soma(x, y), [[3]])

    def test_soma_2x2(self):
        """Testa se a soma das matrizes [[1, 2], [2, 3]] e [[2, 3], [1, 2]] é [[3, 5], [3, 5]]"""
        x: Matriz = [[1, 2], [2, 3]]
        y: Matriz = [[2, 3], [1, 2]]
        self.assertEqual(soma(x, y), [[3, 5], [3, 5]])

    def test_soma_3x3(self):
        """
        Testa se a soma das matrizes [[1, 2, 4], [2, 3, 4], [1, 2, 4]] e
        [[2, 3, 4], [1, 2, 4], [2, 3, 4]] é [[3, 5, 8], [3, 5, 8], [3, 5, 8]]
        """
        x: Matriz = [[1, 2, 4], [2, 3, 4], [1, 2, 4]]
        y: Matriz = [[2, 3, 4], [1, 2, 4], [2, 3, 4]]
        self.assertEqual(soma(x, y), [[3, 5, 8], [3, 5, 8], [3, 5, 8]])
