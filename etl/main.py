import pandas as pd
from pathlib import Path
from extract import Extract
from transform import Transform
from load import Load

if __name__ == "__main__":
    silver, gold, arquivos = Extract()
    arqvs, arqvs_gold = Transform(arquivos)
    Load(arqvs, arqvs_gold, silver, gold)