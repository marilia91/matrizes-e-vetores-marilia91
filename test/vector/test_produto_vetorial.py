"""Esse arquivo testa o arquivo vector.py"""

import unittest  # para criar o caso de teste

from tipos import Vetor
from vector import produto_vetorial as prod_vet


class TestVectorProdutoVetorial(unittest.TestCase):
    """Classe para testar a função produto_vetorial no arquivo vector.py"""

    def test_produto_vetorial_vazia(self):
        """Testa se a resposta é None para vetores vazios"""
        self.assertEqual(prod_vet([], []), None)

    def test_produto_vetorial_incompativel(self):
        """Testa se a resposta é None para vetores incompatíveis"""
        x: Vetor = [1, 2]
        y: Vetor = [1, 2, 3]
        self.assertEqual(prod_vet(x, y), None)

    def test_produto_vetorial_3(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3] e [2, 3, 4]"""
        x: Vetor = [1, 2, 4]
        y: Vetor = [2, 3, 4]
        self.assertEqual(prod_vet(x, y), [-4, 4, -1])

    def test_produto_vetorial_3_2(self):
        """Testa se a resposta é correta para os vetores [0, 0, 0] e [2, 3, 4]"""
        x: Vetor = [0, 0, 0]
        y: Vetor = [2, 3, 4]
        self.assertEqual(prod_vet(x, y), [0, 0, 0])

    def test_produto_vetorial_3_3(self):
        """Testa se a resposta é correta para os vetores [2, 3, 4] e [1, 2, 3]"""
        x: Vetor = [2, 3, 4]
        y: Vetor = [1, 2, 3]
        self.assertEqual(prod_vet(x, y), [1, -2, 1])
