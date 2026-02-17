from extract import Extract
from transform import Transform
from load import Load

#* este arquivo só irá rodar as funções dos outros arquivos
if __name__ == "__main__":
    silver, gold, arquivos = Extract()
    arqvs, arqvs_gold = Transform(arquivos)
    Load(arqvs, arqvs_gold, silver, gold)