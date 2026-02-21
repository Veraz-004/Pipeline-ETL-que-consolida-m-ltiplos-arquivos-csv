from pathlib import Path
import config as c

def relatorio(produto, receita_total_var, dia_max_quantidade, dia_max_receita):
    Path('reports').mkdir(parents=True, exist_ok=True)
    relatorio_prompt=f"""
    === RELATÓRIO ===
    
    O produto mais vendido é: {produto}
    A receita gerada por todas as vendas é: {receita_total_var}
    O dia que teve mais vendas é: {dia_max_quantidade}
    O dia que teve maior montante é: {dia_max_receita}
    """
    with open(c.relatorio, 'w') as arquivo:
        arquivo.write(relatorio_prompt)