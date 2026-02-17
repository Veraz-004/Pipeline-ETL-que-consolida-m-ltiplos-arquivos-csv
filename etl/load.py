import pandas as pd
from pathlib import Path

def Load(arqvs, arqvs_gold, silver, gold):
    df_f_silver=pd.concat(arqvs, ignore_index=True)
    df_f_gold=pd.concat(arqvs_gold, ignore_index=True)
    df_f_silver.to_csv(silver/"silver.csv", index=False)
    df_f_gold.to_csv(gold/"gold.csv", index=False)
    print("Arquivos limpos salvos em: data/silver/silver.csv")
    print("Arquivos prontos para análise salvows em: data/gold/gold.csv")
