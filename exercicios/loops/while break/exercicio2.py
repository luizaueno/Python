#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

total = 0
contador = 0
valor = 0
nome_barato = ''
preco_barato = valor

while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    total += valor
    resposta = input('Deseja continuar? [s/n]: ')
    if valor > 1000:
        contador += 1
    if nome_barato == '':
        preco_barato = valor
        nome_barato = nome
    elif valor < preco_barato:
        preco_barato = valor
        nome_barato = nome
    if resposta == 'n':
        break
print(f'O total da compra é {total:.2f}')
print(f'{contador} produtos custam mais de mil reais')
print(f'{nome_barato} é o produto de menor preço')
