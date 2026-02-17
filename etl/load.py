import pandas as pd
from pathlib import Path

#* Neste arquivo vamos simplesmente criar dois arquivos:
#* O primeiro (silver.csv) irá conter todpos os dados das primeiras pastas, só que limpos
#* o segundo (gold.csv) irá conter métricas baseadas nos dados brutos já prontas para análise
#* E caso as listas do arquivo transform retornarem vazias a operação não será concluída
def Load(arqvs, arqvs_gold, silver, gold):
    if arqvs == []:
        print("Lista de arquivos vazia")
        print("Não foi possível continuar com a operação")
    else:
        df_f_silver=pd.concat(arqvs, ignore_index=True)
        df_f_gold=pd.concat(arqvs_gold, ignore_index=True)
        df_f_silver.to_csv(silver/"silver.csv", index=False)
        df_f_gold.to_csv(gold/"gold.csv", index=False)
        print("Arquivos limpos salvos em: data/silver/silver.csv")
        print("Arquivos prontos para análise salvos em: data/gold/gold.csv")
