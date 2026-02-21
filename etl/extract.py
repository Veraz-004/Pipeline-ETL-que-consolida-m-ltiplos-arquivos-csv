from pathlib import Path
import logging
import config as c
log=logging.getLogger(__name__)
#* Neste arquivo, vamos criar atálhos para os diretórios e pegar todos os dados
def Extract(log):
    arquivos=sorted(c.bronze_dir.glob("*.csv"))
    if not arquivos:
        log.error("Nenhum arquivo .csv encontrado na pasta: data/bronze")
    return arquivos

