# Pipeline ETL para Consolidação de Múltiplos Arquivos CSV

Este projeto implementa uma pipeline ETL (Extract, Transform, Load) em Python para consolidar múltiplos arquivos CSV de vendas, limpar dados inconsistentes e gerar métricas prontas para análise.

Esta pipeline ETL organiza dados de vendas, na qual dentro do arquivo de vendas (formato suportado é o .csv) tenha as informações de:
 - produto (nome do produto vendido)
 - preco (valor do produto vendido)
 - custo (quanto o produto valeu na sua compra pelo vendendor, para que o mesmo possa vende-lo)
 - quantidade (quantidade de produtos vendidos)
 - data (dia na qual o produto foi vendido)

Esta pipeline limpa os dados, e cria métricas para a análise
As métricas criadas estão sendo listadas a baixo:
 - lucro (valor na qual o vendendor ganha em cima da venda do produto. Esta métrica calcula o lucro UNITÁRIO de cada produto)
 - lucro_total (cálculo feito em base do lucro vezes a quantidade de produtos vendidos. Calcula somente o lucro total de cada produto vendido)
 - custo_total (cálculo feito em base do custo vezes a quantidade de produtos vendidos. Calcula somente o custo total de cada produto vendido)
 - receita (cálculo feito em base do preco vezes a quantidade de produtos vendidos. Calcula somente a receira

O objetivo é automatizar o processamento de dados semelhante a ferramentas como Power BI, porém usando Python.

## Estrutura do Projeto

ETL_base/
│
├── data/
│   ├── bronze/   → dados brutos
│   ├── silver/   → dados limpos
│   └── gold/     → dados prontos para análise
│
├── extract.py    → etapa de extração
├── transform.py  → limpeza e criação de métricas
├── load.py       → salvamento dos dados finais
└── main.py       → execução da pipeline

## Como executar

1. Instale as dependências:
pip install -r requirements.txt

2. Coloque os arquivos CSV na pasta:
data/bronze/

3. Execute:
python main.py

## Tecnologias

- Python
- Pandas
- ETL
- Manipulação de dados

## Objetivo

Este projeto foi desenvolvido para prática de engenharia de dados e automação de análise, simulando cenários reais de processamento de dados empresariais.
