"""
Arquivo principal
"""

import time, random
from utils.utils import tempo_gasto


@tempo_gasto
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
    

def gerar_arquivos_facade(quantidade_de_linhas):
  for linhas in quantidade_de_linhas:
    gerar_arquivo(linhas, True)
    gerar_arquivo(linhas, False)


def main() -> None:
  quantidade_de_linhas = [100, 500, 1_000, 5_000, 10_000]
  gerar_arquivos_facade(quantidade_de_linhas)


if __name__ == "__main__":
  main()
