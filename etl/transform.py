import pandas as pd
from pathlib import Path

#* Neste arquivo, os dados brutos vão entrar, e ser separados em df e df_gold
#* O df são os dados originais só que agr sem duplicatas ou células vazias
#* já o df_gold são os dados já limpos e prontos para análise
def Transform(arquivos):
    arqvs=[]
    arqvs_gold=[]
    for arquivo in arquivos:
        opcoes = [
        {"encoding": "utf-8"},
        {"encoding": "utf-8", "sep": ";"},
        {"encoding": "latin1", "sep": ";"}
        ]
        for opcao in opcoes:
            try:
                df = pd.read_csv(arquivo, **opcao)
                break
            except:
                continue
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
            'lucro_total': (df['preco']-df['custo'])*df['quantidade'],
            'data': df['data'],
        })
        arqvs.append(df)
        arqvs_gold.append(df_gold)
    return arqvs, arqvs_gold
#* a função retorna duas listas, uma com os dados originais limpos(arqvs), e outra com os dados para análise(arqvs_gold)