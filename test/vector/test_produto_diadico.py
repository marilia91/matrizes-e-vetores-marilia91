"""Esse arquivo testa o arquivo vector.py"""

import unittest  # for creating the test case

from tipos import Vetor
from vector import produto_diadico as prod


class TestVectorProdutoDiadico(unittest.TestCase):
    """Classer para testar a função produto_diádico no arquivo vector.py"""

    def test_produto_diadico_vazio(self):
        """Testa se a resposta é vazia para vetores vazios"""
        self.assertEqual(prod([], []), [])

    def test_produto_diadico_incompativel(self):
        """Testa se a resposta é None para vetores de tamanhos diferentes"""
        self.assertEqual(prod([1, 2], [1]), None)

    def test_produto_diadico_1(self):
        """Testa se a resposta é correta para os vetores [1] e [2]"""
        x: Vetor = [1]
        y: Vetor = [2]
        self.assertEqual(prod(x, y), [[2]])

    def test_produto_diadico_2(self):
        """Testa se a resposta é correta para os vetores [1, 2] e [2, 3]"""
        x: Vetor = [1, 2]
        y: Vetor = [2, 3]
        self.assertEqual(prod(x, y), [[2, 3], [4, 6]])

    def test_produto_diadico_3(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3] e [2, 3, 4]"""
        x: Vetor = [1, 2, 3]
        y: Vetor = [2, 3, 4]
        self.assertEqual(prod(x, y), [[2, 3, 4], [4, 6, 8], [6, 9, 12]])

    def test_produto_diadico_4(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3, 4] e [2, 3, 4, 5]"""
        x: Vetor = [1, 2, 3, 4]
        y: Vetor = [2, 3, 4, 5]
        self.assertEqual(
            prod(x, y), [[2, 3, 4, 5], [4, 6, 8, 10], [6, 9, 12, 15], [8, 12, 16, 20]]
        )
