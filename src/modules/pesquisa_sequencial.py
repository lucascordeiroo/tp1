"""
Arquivo que contém a estrutura de dados pesquisa sequencial
"""

def pesquisa_sequencial(nome_do_arquivo, chave):
  numero_de_comparacoes = 0

  with open(nome_do_arquivo, "r") as arquivo:
    for linha in arquivo:
      numero_de_comparacoes = numero_de_comparacoes + 1
      partes = linha.strip().split(",")
      if partes[0] == chave:
        print(f'chave encontrada na linha {linha}')

  return numero_de_comparacoes
