import pandas as pd
from pathlib import Path
def extract():
    #*Criando caminhos
    bronze=Path("data/bronze")
    prata=Path("data/prata")
    ouro=Path("data/ouro")
    arquivos=sorted(bronze.glob("*.csv"))
    prata.mkdir(parents=True, exist_ok=True)
    ouro.mkdir(parents=True, exist_ok=True)
    return arquivos, prata, ouro

def transform(arquivos):
    #*criando a lista e limpando os arquivos
    arqvs=[]
    arqvs_ouro=[]
    for arquivo in arquivos:
        df=pd.read_csv(arquivo)
        df["preco"]= pd.to_numeric(df["preco"], errors="coerce")
        df["custo"]= pd.to_numeric(df["custo"], errors="coerce")
        df["quantidade"]= pd.to_numeric(df["quantidade"], errors="coerce")
        df["data"]= pd.to_datetime(df["data"], errors="coerce")
        df=df.dropna(subset=["preco", "produto", "quantidade", "custo", "data"])
        df=df.drop_duplicates(subset=["preco", "produto", "quantidade", "custo", "data"])
        #*criando a  parte de receita, lucro, lucros e custos totais e adicionando tudo a lista arqvs
        df_ouro = pd.DataFrame({
            "produto": df["produto"],
            'receita': df['preco'] * df['quantidade'],
            'custo_total': df['custo'] * df['quantidade'],
            'lucro_total': (df['preco'] - df['custo']) * df['quantidade'],
            'data': df['data'],
        })
        arqvs.append(df)
        arqvs_ouro.append(df_ouro)
        return arqvs, arqvs_ouro

def load(arqvs, arqvs_ouro, prata, ouro):
    #*fazendo um df final com pdconcat e criando um arquivo prata csv e um ouro csv para análise
    df_final_prata=pd.concat(arqvs, ignore_index=True)
    df_final_ouro=pd.concat(arqvs_ouro, ignore_index=True)
    df_final_prata.to_csv(prata/"vendas_prata.csv", index=False)
    df_final_ouro.to_csv(ouro/"vendas_ouro.csv", index=False)
    print("Informações limpas em data/prata/vendas_prata.csv")
    print("Informações para análise em data/ouro/vendas_ouro.csv")


#*Rodando as funções
if __name__ == "__main__":
    arquivos, prata, ouro = extract()
    arqvs, arqvs_ouro = transform(arquivos)
    load(arqvs, arqvs_ouro, prata, ouro)
