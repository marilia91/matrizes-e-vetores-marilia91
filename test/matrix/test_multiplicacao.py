"""Esse arquivo testa o arquivo matrix.py"""

import unittest

from matrix import multiplicacao as multi
from tipos import Matriz


class TestMatrixMultiplicacao(unittest.TestCase):
    """Classe para testar a função multiplicação no arquivo matrix.py"""

    def test_multiplicacao_vazia(self):
        """Testa se a resposta é vazia para matrizes vazias"""
        self.assertEqual(multi([], []), [])

    def test_multiplicacao_incompativel(self):
        """Testa se a multiplicação de matrizes incompatíveis é None"""
        x: Matriz = [[1, 2], [3, 4]]
        y: Matriz = [[1], [2], [3]]
        self.assertEqual(multi(x, y), None)

    def test_multiplicacao_1x1(self):
        """Testa se a multiplicação de matrizes 1x1 é feita corretamente"""
        x: Matriz = [[1]]
        y: Matriz = [[2]]
        self.assertEqual(multi(x, y), [[2]])
        self.assertEqual(multi(y, x), [[2]])  # pylint: disable=arguments-out-of-order
        self.assertEqual(multi(x, x), [[1]])
        self.assertEqual(multi(y, y), [[4]])

    def test_multiplicacao_1x2_2x1(self):
        """Testa se a multiplicação de matrizes 1x2 com 2x1 é feita corretamente"""
        x: Matriz = [[1, 2]]
        y: Matriz = [[2], [3]]
        self.assertEqual(multi(x, y), [[8]])

    def test_multiplicacao_2x2_2x2(self):
        """Testa se a multiplicação de matrizes 2x2 com 2x2 é feita corretamente"""
        x: Matriz = [[1, 2], [3, 4]]
        y: Matriz = [[2, 3], [4, 5]]
        self.assertEqual(multi(x, y), [[10, 13], [22, 29]])

    def test_multiplicacao_2x3_3x2(self):
        """Testa se a multiplicação de matrizes 2x3 com 3x2 é feita corretamente"""
        x: Matriz = [[1, 2, 3], [4, 5, 6]]
        y: Matriz = [[2, 3], [4, 5], [6, 7]]
        self.assertEqual(multi(x, y), [[28, 34], [64, 79]])

    def test_multiplicacao_3x3_3x3(self):
        """Testa se a multiplicação de matrizes 3x3 com 3x3 é feita corretamente"""
        x: Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y: Matriz = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
        self.assertEqual(multi(x, y), [[36, 42, 48], [81, 96, 111], [126, 150, 174]])
