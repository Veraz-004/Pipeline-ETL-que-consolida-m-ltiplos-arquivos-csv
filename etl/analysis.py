import pandas as pd
from pathlib import Path
import logging
log=logging.getLogger(__name__)

def lucro_max(df, log):
    lucro_max=df['lucro_total'].max() 
    linha=df[df['lucro_total'] == lucro_max]
    produto = linha['produto'].iloc[0]
    return produto

def receita_total(df, log):
    receita_total_var=df['receita'].sum()
    return receita_total_var


def dia_quantidade(df, log):
    vendas_por_dia= df.groupby('data')['quantidade'].sum()
    dia_max_quantidade=vendas_por_dia.idxmax()
    return dia_max_quantidade

def dia_receita(df, log):
    receita_por_dia=df.groupby('data')['receita'].sum()
    dia_max_receita=receita_por_dia.idxmax()
    return dia_max_receita
