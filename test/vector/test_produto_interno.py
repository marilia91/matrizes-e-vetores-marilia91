"""Esse arquivo testa o arquivo vector.py"""

import unittest

from tipos import Vetor
from vector import produto_interno as pi


class TestVectorProdutoInterno(unittest.TestCase):
    """ "Classe para testar a função produto_interno no arquivo vector.py"""

    def test_produto_interno_vazio(self):
        """Testa se a resposta é 0 para vetores vazios"""
        self.assertEqual(pi([], []), 0)

    def test_produto_interno_incompativel(self):
        """Testa se a resposta é None para vetores de tamanhos diferentes"""
        self.assertEqual(pi([1, 2], [1]), None)

    def test_produto_interno_1(self):
        """Testa se a resposta é correta para os vetores [1] e [1]"""
        x: Vetor = [1]
        y: Vetor = [1]
        self.assertEqual(pi(x, y), 1)

    def test_produto_interno_1_negativo(self):
        """Testa se a resposta é correta para os vetores [1] e [-1]"""
        x: Vetor = [1]
        y: Vetor = [-1]
        self.assertEqual(pi(x, y), -1)

    def test_produto_interno_2(self):
        """Testa se a resposta é correta para os vetores [1, 2] e [1, 2]"""
        x: Vetor = [1, 2]
        y: Vetor = [1, 2]
        self.assertEqual(pi(x, y), 5)

    def test_produto_interno_2_negativo(self):
        """Testa se a resposta é correta para os vetores [1, 2] e [-1, -2]"""
        x: Vetor = [1, 2]
        y: Vetor = [-1, -2]
        self.assertEqual(pi(x, y), -5)

    def test_produto_interno_3(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3] e [1, 2, 3]"""
        x: Vetor = [1, 2, 3]
        y: Vetor = [1, 2, 3]
        self.assertEqual(pi(x, y), 14)

    def test_produto_interno_3_negativo(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3] e [-1, -2, -3]"""
        x: Vetor = [1, 2, 3]
        y: Vetor = [-1, -2, -3]
        self.assertEqual(pi(x, y), -14)
