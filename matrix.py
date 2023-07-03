"""Módulo com as funções de manipulação de matrizes."""
from tipos import Escalar, Matriz


def soma(x: Matriz, y: Matriz) -> Matriz | None:
    """Soma duas matrizes"""
    # TODO: implementar
    # a soma de duas matrizes [[1, 2, 4], [2, 3, 4]] + [[2, 3, 4], [1, 2, 4]]
    # é [[3, 5, 8], [3, 5, 8]] a soma só pode ser realizada se as matrizes tem
    # a mesma quantidade de linhas e colunas.
    # caso contrário, deve retornar None
    raise NotImplementedError


def multiplicacao_por_escalar(matriz: Matriz, escalar: Escalar) -> Matriz:
    """Multiplica uma matriz por um escalar"""
    # TODO: implementar
    # a multiplicação de uma matriz [[1, 2, 4], [2, 3, 4]]
    # por um escalar 2 é [[2, 4, 8], [4, 6, 8]]
    raise NotImplementedError


def multiplicacao(x: Matriz, y: Matriz) -> Matriz | None:
    """Multiplica duas matrizes"""
    # TODO: implementar
    # a multiplicação de duas matrizes [[1, 2, 4], [2, 3, 4]]
    # por [[2, 3, 4], [1, 2, 4]] é [[10, 17, 28], [12, 20, 32]]
    # a multiplicação só pode ser realizada
    # se a quantidade de colunas da primeira matriz é
    # igual a quantidade de linhas da segunda matriz.
    # caso contrário, deve retornar None
    raise NotImplementedError


def norma(x: Matriz) -> Escalar:
    """Calcula a norma de uma matriz"""
    # TODO: implementar
    # a norma de uma matriz [[1, 2, 4], [2, 3, 4]] é 6.928203230275509
    # ela consiste em calcular a raiz quadrada da
    # soma dos quadrados dos elementos da matriz
    # caso a matriz esteja vazia deve-se retornar 0
    raise NotImplementedError


def eh_simetrica(x: Matriz) -> bool:
    """Verifica se uma matriz é simétrica"""
    # TODO: implementar
    # uma matriz é simétrica se ela é quadrada e se ela é igual a sua transposta
    # a transposta de uma matriz é a matriz que tem as linhas da
    # matriz original como colunas e as colunas da matriz original como linhas
    raise NotImplementedError


def transposta(x: Matriz) -> Matriz:
    """Calcula a transposta de uma matriz"""
    # TODO: implementar
    # a transposta de uma matriz [[1, 2, 4], [2, 3, 4]] é [[1, 2], [2, 3], [4, 4]]
    raise NotImplementedError
