import pandas as pd
from pathlib import Path

def Transform(arquivos):
    arqvs=[]
    arqvs_gold=[]
    for arquivo in arquivos:
        df=pd.read_csv(arquivo)
        df["preco"]=pd.to_numeric(df["preco"], errors="coerce")
        df["quantidade"]=pd.to_numeric(df["quantidade"], errors="coerce")
        df["custo"]=pd.to_numeric(df["custo"], errors="coerce")
        df["data"]=pd.to_datetime(df["data"], errors="coerce")
        df=df.dropna(subset=['preco', 'produto', 'custo', 'quantidade', 'data'])
        df=df.drop_duplicates(subset=['preco', 'produto', 'custo', 'quantidade', 'data'])
        df_gold=pd.DataFrame({
            'produto': df['produto'],
            'receita': df['preco']*df['quantidade'],
            'custo_total': df['custo']*df['quantidade'],
            'lucro_total': (df['preco']-df['quantidade'])*df['quantidade'],
            'data': df['data'],
        })
        arqvs.append(df)
        arqvs_gold.append(df_gold)
    return arqvs, arqvs_gold