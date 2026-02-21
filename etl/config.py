from pathlib import Path

data=Path('data')
bronze_dir=Path('data/bronze')
silver_dir=Path('data/silver')
silver_data=Path('data/silver/silver.csv')
gold_dir=Path('data/gold')
gold_data=Path('data/gold/gold.csv')
logs_dir=Path("logs")
logs=Path("logs/pipeline.log")
relatorio_dir=Path("report")
relatorio=Path("report/relatorio.txt")

def diretorios(data, bronze_dir, silver_dir, gold_dir, logs_dir, relatorio_dir):
    data.mkdir(parents=True, exist_ok=True)
    bronze_dir.mkdir(parents=True, exist_ok=True)
    silver_dir.mkdir(parents=True, exist_ok=True)
    gold_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    relatorio_dir.mkdir(parents=True, exist_ok=True)