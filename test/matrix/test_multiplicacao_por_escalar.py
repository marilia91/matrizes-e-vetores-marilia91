"""Esse arquivo testa o arquivo matrix.py"""

import unittest  # for creating the test case

from matrix import multiplicacao_por_escalar as multi
from tipos import Matriz


class TestMatrixMultiplicacaoPorEscalar(unittest.TestCase):
    """Classe para testar a função multiplicação_por_escalar no arquivo matrix.py"""

    def test_multiplicacao_por_escalar_vazia(self):
        """Testa se a resposta é vazia para matrizes vazias"""
        self.assertEqual(multi([], 0), [])

    def test_multiplicacao_por_escalar_1x1(self):
        """Testa se a multiplicação da matriz [[1]] por 2, 3 e 0 é feita corretamente"""
        x: Matriz = [[1]]
        self.assertEqual(multi(x, 2), [[2]])
        self.assertEqual(multi(x, 3), [[3]])
        self.assertEqual(multi(x, 0), [[0]])

    def test_multiplicacao_por_escalar_1x2(self):
        """Testa se a multiplicação da matriz [[1, 2]] por 2, 3 e 0 é feita corretamente"""
        x: Matriz = [[1, 2]]
        self.assertEqual(multi(x, 2), [[2, 4]])
        self.assertEqual(multi(x, 3), [[3, 6]])
        self.assertEqual(multi(x, 0), [[0, 0]])

    def test_multiplicacao_por_escalar_2x1(self):
        """Testa se a multiplicação da matriz [[1], [2]] por 2, 3 e 0 é feita corretamente"""
        x: Matriz = [[1], [2]]
        self.assertEqual(multi(x, 2), [[2], [4]])
        self.assertEqual(multi(x, 3), [[3], [6]])
        self.assertEqual(multi(x, 0), [[0], [0]])

    def test_multiplicacao_por_escalar_2x2(self):
        """Testa se a multiplicação da matriz [[1, 2], [3, 4]] por 2, 3 e 0 é feita corretamente"""
        x: Matriz = [[1, 2], [3, 4]]
        self.assertEqual(multi(x, 2), [[2, 4], [6, 8]])
        self.assertEqual(multi(x, 3), [[3, 6], [9, 12]])
        self.assertEqual(multi(x, 0), [[0, 0], [0, 0]])
