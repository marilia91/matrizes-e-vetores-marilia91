"""Esse arquivo testa o arquivo matrix.py"""

import unittest  # for creating the test case

from matrix import eh_simetrica
from tipos import Matriz


class TestMatrixEhSimetrica(unittest.TestCase):
    """Classe para testar a função é_simétrica no arquivo matrix.py"""

    def test_eh_simetrica_vazia(self):
        """Testa se a resposta é True para matrizes vazias"""
        self.assertEqual(eh_simetrica([]), True)

    def test_eh_simetrica_1x1(self):
        """Testa se a resposta é True para a matriz [[1]]"""
        x: Matriz = [[1]]
        self.assertEqual(eh_simetrica(x), True)

    def test_eh_simetrica_2x2(self):
        """Testa se a resposta é True para a matriz [[1, 2], [2, 1]]"""
        x: Matriz = [[1, 2], [2, 1]]
        self.assertEqual(eh_simetrica(x), True)

    def test_eh_simetrica_2x2_false(self):
        """Testa se a resposta é False para a matriz [[1, 3], [2, 3]]"""
        x: Matriz = [[1, 3], [2, 3]]
        self.assertEqual(eh_simetrica(x), False)

    def test_eh_simetrica_3x3(self):
        """Testa se a resposta é True para a matriz [[1, 2, 4], [2, 3, 4], [4, 4, 4]]"""
        x: Matriz = [[1, 2, 4], [2, 3, 4], [4, 4, 4]]
        self.assertEqual(eh_simetrica(x), True)

    def test_eh_simetrica_3x3_false(self):
        """Testa se a resposta é False para a matriz [[1, 2, 1], [2, 3, 4], [1, 2, 4]]"""
        x: Matriz = [[1, 2, 1], [2, 3, 4], [1, 2, 4]]
        self.assertEqual(eh_simetrica(x), False)
