import pandas as pd
from pathlib import Path

def Extract():
    bronze=Path("data/bronze")
    silver=Path("data/silver")
    gold=Path("data/gold")
    arquivos=sorted(bronze.glob("*.csv"))
    return silver, gold, arquivos
