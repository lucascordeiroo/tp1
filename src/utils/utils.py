"""
Arquivo com funções uteis que podem ser reutilizadas
"""

import time, random


def tempo_gasto(funcao):
  def wrapper(*args, **kwargs):
    tempo_inicial = time.time()
    funcao(*args, **kwargs)
    tempo_final = time.time() - tempo_inicial
    print(f'{tempo_final:.6f}')
  return wrapper


def gerar_arquivo(linhas: int, chaves_ordenadas: bool) -> None:
  nome_do_arquivo = f'arquivos_entrada/{linhas}_desordenado.txt'
  ids = random.sample(range(linhas), linhas)

  if chaves_ordenadas:
    nome_do_arquivo = f'arquivos_entrada/{linhas}.txt'
    ids = range(linhas)

  with open(nome_do_arquivo, "w") as arquivo:
    for i in range(linhas):
      linha = f'{ids[i]},12345,AOEUAOEUASTOEUHAOSENTUHAOSENTUHAS\n'
      arquivo.write(linha)
