"""
Faturamento do Melhor e do Pior Mês do Ano
Qual foi o valor de vendas do melhor mês do Ano? E valor do pior mês do ano?
"""
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
lista_porcent_ano = []

vendas_ano = vendas_1sem + vendas_2sem #unindo as 2 listas

melhor_mes = vendas_ano.index(max(vendas_ano)) #max = retorna a posição com o maior valor

pior_mes = vendas_ano.index(min(vendas_ano)) #min = retorna a posição com o menor valor

soma_ano = sum(vendas_ano) #sum = soma todos os valores da lista

#obj.: percorre a lista vendas_ano e encontrar quanto esse valor representou no fat do ano

for valor in vendas_ano:
    lista_porcent_ano.append(valor/soma_ano*100)

print("\nO mês de {} foi o de melhor faturamento R${:.2f} do ano e representou {:.2f}% do fat.".format(meses[melhor_mes],vendas_ano[melhor_mes],lista_porcent_ano[melhor_mes]))

print("\nO mês de {} foi o pior faturamento R${:.2f} do ano e representou {:.2f}% do fat.".format(meses[pior_mes],vendas_ano[pior_mes], lista_porcent_ano[pior_mes]))

print("\n\n\tTOP 3º\n\n")

top1 = vendas_ano.pop()

