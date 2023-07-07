"""Módulo com as funções de manipulação de matrizes."""
from tipos import Escalar, Matriz


def soma(x: Matriz, y: Matriz) -> Matriz | None:
    """Soma duas matrizes"""
    if x == [] and y == []:
        return []

    if len(x) != len(y) or len(x[0]) != len(y[0]):
        return None

    linha = len(x)
    coluna = len(x[0])

    msoma = []
    for i in range(linha):
        msoma.append([])
        for j in range(coluna):
            msoma[i].append(0)

    for i in range(linha):
        for j in range(coluna):
            msoma[i][j] = x[i][j] + y[i][j]

    return msoma


def multiplicacao_por_escalar(matriz: Matriz, escalar: Escalar) -> Matriz:
    """Multiplica uma matriz por um escalar"""
    
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return []
    linha = len(matriz)
    coluna = len(matriz[0])
    linha = len(matriz)
    coluna = len(matriz[0])
    
    prod_escalar = []
    for i in range(0, linha):
        prod_escalar.append([])
        for j in range(0, coluna):
            prod_escalar[i].append(0)
    
    for i in range(0, linha):
        for j in range(0, coluna):
            prod_escalar[i][j] = matriz[i][j] * escalar
    return prod_escalar


def multiplicacao(x: Matriz, y: Matriz) -> Matriz | None:
    """Multiplica duas matrizes"""
    
    linha_x = len(x)
    coluna_x = len(x[0]) if linha_x > 0 else 0
    linha_y = len(y)
    coluna_y = len(y[0]) if linha_y > 0 else 0

    if coluna_x != linha_y:
        return None

    resultado = [[0] * coluna_y for _ in range(linha_x)]

    for i in range(linha_x):
        for j in range(coluna_y):
            for k in range(coluna_x):
                resultado[i][j] += x[i][k] * y[k][j]

    return resultado


def norma(x: Matriz) -> Escalar:
    """Calcula a norma de uma matriz"""
    
    if len(x) == 0:
        return 0
    linha = len(x)
    coluna = len(x[0])
    soma = 0
    for i in range(0, linha):
        for j in range(0, coluna):
            soma += (x[i][j]) ** 2
    norma = soma**0.5
    return norma


def eh_simetrica(x: Matriz) -> bool:
    """Verifica se uma matriz é simétrica"""
    
    linha = len(x)
    if linha == 0:
        return True

    coluna = len(x[0])

    if linha != coluna:
        return False

    for i in range(linha):
        for j in range(coluna):
            if x[i][j] != x[j][i]:
                return False

    return True


def transposta(x: Matriz) -> Matriz:
    """Calcula a transposta de uma matriz"""
    
    if not x:
        return []

    linha = len(x)
    coluna = len(x[0])

    m_transposta = [[0] * linha for _ in range(coluna)]

    for i in range(linha):
        for j in range(coluna):
            m_transposta[j][i] = x[i][j]

    return m_transposta