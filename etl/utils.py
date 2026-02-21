import logging
import config as c
import pandas as pd
lod=logging.getLogger(__name__)

def data_verify(log):
    if not c.gold_data.exists():
        log.warning("Arquivo gold.csv não encontrado.")
        return None
    df=pd.read_csv(c.gold_data)
    if df.empty:
        log.warning("Arquivo gold.csv exixte, mas vazio")
        return None
    return df