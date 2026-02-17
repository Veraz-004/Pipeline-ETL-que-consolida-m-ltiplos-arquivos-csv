from pathlib import Path

#* Neste arquivo, vamos criar atálhos para os diretórios e pegar todos os dados
def Extract():
    bronze=Path("data/bronze")
    silver=Path("data/silver")
    gold=Path("data/gold")
    bronze.mkdir(parents=True, exist_ok=True)
    silver.mkdir(parents=True, exist_ok=True)
    gold.mkdir(parents=True, exist_ok=True)
    arquivos=sorted(bronze.glob("*.csv"))
    return silver, gold, arquivos
