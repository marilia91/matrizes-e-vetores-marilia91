"""Módulo com as funções de manipulação de vetores."""

from tipos import Escalar, Vetor

import math


def norma(x: Vetor) -> Escalar | None:
    """Calcula a norma de um vetor"""
    if len(x) == 0:
        return None

    sum_quadrados = sum([elem**2 for elem in x])
    norma = math.sqrt(sum_quadrados)
    return norma


def soma(x: Vetor, y: Vetor) -> Vetor | None:
    """Soma dois vetores"""
    if len(x) != len(y):
        return None

    vetor_sum = [x[i] + y[i] for i in range(len(x))]
    return vetor_sum


def multiplicacao_por_escalar(vetor: Vetor, escalar: Escalar) -> Vetor:
    """Multiplica um vetor por um escalar"""

    vetor_mult = [elem * escalar for elem in vetor]
    return vetor_mult


def produto_interno(x: Vetor, y: Vetor) -> Escalar | None:
    """Calcula o produto interno de dois vetores"""

    if len(x) != len(y):
        return None

    prod = sum([x[i] * y[i] for i in range(len(x))])
    return prod


def produto_vetorial(x: Vetor, y: Vetor) -> Vetor | None:
    """Calcula o produto vetorial de dois vetores"""
    
    if len(x) != 3 or len(y) != 3:
        return None

    prod_vet = [
        x[1] * y[2] - x[2] * y[1],
        x[2] * y[0] - x[0] * y[2],
        x[0] * y[1] - x[1] * y[0],
    ]
    return prod_vet


def produto_diadico(x: Vetor, y: Vetor) -> list[Vetor] | None:
    """Calcula o produto diádico de dois vetores"""
    
    if len(x) != len(y):
        return None

    prod_diatico = [[x[i] * y[j] for j in range(len(y))] for i in range(len(x))]
    return prod_diatico
