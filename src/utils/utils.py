"""
Arquivo com funções uteis que podem ser reutilizadas
"""

import time


def tempo_gasto(funcao):
  def wrapper(*args, **kwargs):
    tempo_inicial = time.time()
    funcao(*args, **kwargs)
    tempo_final = time.time() - tempo_inicial
    print(f'{tempo_final:.6f}')
  return wrapper
