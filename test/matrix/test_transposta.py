"""Esse arquivo testa o arquivo matrix.py"""

import unittest  # for creating the test case

from matrix import transposta
from tipos import Matriz


class TestMatrixTransposta(unittest.TestCase):
    """Classe para testar a função transposta no arquivo matrix.py"""

    def test_transposta_vazia(self):
        """Testa se a resposta é vazia para matriz vazia"""
        self.assertEqual(transposta([]), [])

    def test_transposta_1x1(self):
        """Testa se a resposta é correta para a matriz [[1]]"""
        x: Matriz = [[1]]
        self.assertEqual(transposta(x), [[1]])

    def test_transposta_2x2(self):
        """Testa se a resposta é correta para a matriz [[1, 2], [2, 3]]"""
        x: Matriz = [[1, 2], [2, 3]]
        self.assertEqual(transposta(x), [[1, 2], [2, 3]])

    def test_transposta_2x3(self):
        """Testa se a resposta é correta para a matriz [[1, 2, 4], [2, 3, 4]]"""
        x: Matriz = [[1, 2, 4], [2, 3, 4]]
        self.assertEqual(transposta(x), [[1, 2], [2, 3], [4, 4]])

    def test_transposta_3x2(self):
        """Testa se a resposta é correta para a matriz [[1, 2], [2, 3], [1, 2]]"""
        x: Matriz = [[1, 2], [2, 3], [1, 2]]
        self.assertEqual(transposta(x), [[1, 2, 1], [2, 3, 2]])

    def test_transposta_3x3(self):
        """Testa se a resposta é correta para a matriz [[1, 2, 4], [2, 3, 4], [1, 2, 4]]"""
        x: Matriz = [[1, 2, 4], [2, 3, 4], [1, 2, 4]]
        self.assertEqual(transposta(x), [[1, 2, 1], [2, 3, 2], [4, 4, 4]])
