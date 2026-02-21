import logging
from pathlib import Path
import extract
import load
import config as c
import analysis as a
import transform
import relatório
import utils
Path("logs").mkdir(parents=True, exist_ok=True)
log=logging.getLogger(__name__)


logging.basicConfig(
    level=logging.INFO,
    format=" %(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
    
)

def ETL():
    arquivos = extract.Extract(log)
    arqvs, arqvs_gold=transform.Transform(arquivos, log)
    load.Load(arqvs, arqvs_gold, log)


if __name__ == "__main__":
    c.diretorios(c.data, c.bronze_dir, c.silver_dir, c.gold_dir, c.logs_dir, c.relatorio_dir)
    ETL()
    df = utils.data_verify(log)
    if df is None or df.empty:
        log.error("Nenhum dado para criar métricas")
    else:
        produto = a.lucro_max(df, log)
        receita_total_var = a.receita_total(df, log)
        dia_max_quantidade = a.dia_quantidade(df, log)
        dia_max_receita = a.dia_receita(df, log)
        relatório.relatorio(produto, receita_total_var, dia_max_quantidade, dia_max_receita)
        log.info(f"Métricas criadas e salvas em: {c.relatorio}")
        log.info("Operação concluida com sucesso")