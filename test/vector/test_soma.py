"""Esse arquivo testa o arquivo vector.py"""

import unittest  # para criar o caso de teste

from tipos import Vetor
from vector import soma


class TestVectorSoma(unittest.TestCase):
    """Classe para testar a função soma no arquivo vector.py"""

    def test_soma_vazia(self):
        """Testa se a resposta é vazia para vetores vazios"""
        self.assertEqual(soma([], []), [])

    def test_soma_incompativel(self):
        """Testa se a soma de vetores incompatíveis é None"""
        x: Vetor = [1, 2]
        y: Vetor = [1, 2, 3]
        self.assertEqual(soma(x, y), None)

    def test_soma_1(self):
        """Testa se a resposta é correta para os vetores [1] e [1]"""
        x: Vetor = [1]
        y: Vetor = [1]
        self.assertEqual(soma(x, y), [2])

    def test_soma_2(self):
        """Testa se a resposta é correta para os vetores [1, 2] e [1, 2]"""
        x: Vetor = [1, 2]
        y: Vetor = [1, 2]
        self.assertEqual(soma(x, y), [2, 4])

    def test_soma_3(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3] e [1, 2, 3]"""
        x: Vetor = [1, 2, 3]
        y: Vetor = [1, 2, 3]
        self.assertEqual(soma(x, y), [2, 4, 6])

    def test_soma_4(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3, 4] e [4, 3, 2, 1]"""
        x: Vetor = [1, 2, 3, 4]
        y: Vetor = [4, 3, 2, 1]
        self.assertEqual(soma(x, y), [5, 5, 5, 5])

    def test_soma_comutativa(self):
        """Testa se a soma é comutativa"""
        x: Vetor = [1, 2, 3, 4]
        y: Vetor = [4, 3, 2, 1]
        self.assertEqual(
            soma(x, y), soma(y, x)  # pylint: disable=arguments-out-of-order
        )
