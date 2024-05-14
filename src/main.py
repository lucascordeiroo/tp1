"""
Arquivo principal
"""

from utils.utils import tempo_gasto, gerar_arquivo


def gerar_arquivos_facade(quantidade_de_linhas):
  for linhas in quantidade_de_linhas:
    gerar_arquivo(linhas, True)
    gerar_arquivo(linhas, False)


def main() -> None:
  quantidade_de_linhas = [100, 500, 1_000, 5_000, 10_000]
  gerar_arquivos_facade(quantidade_de_linhas)


if __name__ == "__main__":
  main()
