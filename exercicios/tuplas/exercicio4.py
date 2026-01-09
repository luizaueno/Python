'''
 Crie uma tupla com valores de vendas realizadas durante um dia (valores inteiros).

O programa deve:

Mostrar todas as vendas

Informar quantas vendas foram maiores que 100

Mostrar o total arrecadado

Mostrar a posição da primeira venda igual a 50, caso exista
'''
print('-' * 60)
vendas = (150, 100, 300, 780, 180, 1050, 50, 2000, 450, 120)
print(f'Os valores das vendas do dia foram: {vendas}')
print('-' * 60)
cont = 0
for v in vendas:
    if v > 100:
        cont += 1
print(f'{cont} vendas foram maior que 100 reais')
print('-' * 60)
t = 0
for v in vendas:
    t += v
print(f'O total das vendas do dia foi: {t} reais')
print('-' * 60)
for pos, v in enumerate(vendas):
    if v == 50:
        print(f'A primeira venda de 50 reais aconteceu na posição {pos +1}')
        break
print('-' * 60)

