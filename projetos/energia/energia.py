'''
calcule quanto um aparelho gasta de energia em um mês.
deve pedir: potencia em watts float, horas de uso float, preço do Kwh float
calcular e mostrar:
    - Consumo diário = potência × horas / 1000
    - Consumo mensal = consumo diário × 30
    - Custo mensal = consumo mensal × preço do kWh
'''

pot = float(input('Qual a potência em watts desse aparelho? '))
h = float(input('Quantas horas por dia é utilizado? '))
preco = float(input('Qual é o preço do Kwh? '))
consumo_d = (pot * h)/1000
consumo_m = consumo_d * 30
custo_m = consumo_m * preco

print('O consumo diário é igual a {:.2f} Kwh, o mensal é: {:.2f} Kwh e o custo mensal é de R$ {:.2f} '.format(consumo_d, consumo_m, custo_m))
