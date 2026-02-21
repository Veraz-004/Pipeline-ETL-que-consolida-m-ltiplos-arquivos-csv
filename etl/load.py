import pandas as pd
from pathlib import Path
import logging
import config as c
log=logging.getLogger(__name__)
#* Neste arquivo vamos simplesmente criar dois arquivos:
#* O primeiro (silver.csv) irá conter todpos os dados das primeiras pastas, só que limpos
#* o segundo (gold.csv) irá conter métricas baseadas nos dados brutos já prontas para análise
#* E caso as listas do arquivo transform retornarem vazias a operação não será concluída
def Load(arqvs, arqvs_gold, log):
    if arqvs == []:
        log.error("Lista de dados vazia")
        log.warning("Não foi possivel continuar a operação")
    else:
        df_f_silver=pd.concat(arqvs, ignore_index=True)
        df_f_gold=pd.concat(arqvs_gold, ignore_index=True)
        log.info("Dados empilhados com sucesso")
        df_f_silver.to_csv(c.silver_data, index=False)
        df_f_gold.to_csv(c.gold_data, index=False)
        log.info("Arquivos limpos salvos em: data/silver/silver.csv")
        log.info("Arquivos prontos para análise salvos em: data/gold/gold.csv")
