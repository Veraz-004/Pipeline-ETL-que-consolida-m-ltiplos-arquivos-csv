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
