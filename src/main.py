"""
Arquivo principal
"""

import time, random

def tempo_gasto(funcao):
  def wrapper(*args, **kwargs):
    tempo_inicial = time.time()
    funcao(*args, **kwargs)
    tempo_final = time.time() - tempo_inicial
    print(f'{tempo_final:.6f}')
  return wrapper


@tempo_gasto
def gerar_arquivo(linhas, chaves_ordenadas) -> None:
 nome_do_arquivo = f'arquivos_entrada/{linhas}_desordenado.txt'
 ids = random.sample(range(linhas), linhas)

 if chaves_ordenadas:
   nome_do_arquivo = f'arquivos_entrada/{linhas}.txt'
   ids = range(linhas)

 with open(nome_do_arquivo, "w") as arquivo:
  for i in range(linhas):
    linha = f'{ids[i]},12345,AOEUAOEUASTOEUHAOSENTUHAOSENTUHAS\n'
    arquivo.write(linha)
    

def gerar_arquivos_facade():
  gerar_arquivo(100, True)
  gerar_arquivo(500, True)
  gerar_arquivo(1_000, True)
  gerar_arquivo(5_000, True)
  gerar_arquivo(10_000, True)
  gerar_arquivo(100, False)
  gerar_arquivo(500, False)
  gerar_arquivo(1_000, False)
  gerar_arquivo(5_000, False)
  gerar_arquivo(10_000, False)


def pesquisa_sequencial(nome_do_arquivo, chave):
  with open(nome_do_arquivo, "r") as arquivo:
    for linha in arquivo:
      partes = linha.strip().split(",")
      if partes[0] == chave:
        print(f'chave encontrada na linha {linha}')


def main() -> None:
  gerar_arquivos_facade()

if __name__ == "__main__":
  main()
