'''
Crie uma lista chamada compras com pelo menos 5 itens (strings).
Depois faça:

Mostre todos os itens da lista.

Adicione mais 2 itens usando append().

Remova 1 item específico usando remove().

Mostre a lista em ordem alfabética com sort().

Conte quantos itens tem no total com len().
'''

compras = ['pão', 'ovos', 'leite', 'frango', 'sorvete']
print(compras)
print('-' * 70)
compras.append('arroz')
compras.append('macarrao')
print(compras)
print('-' * 70)
compras.remove('pão')
print(compras)
print('-' * 70)
compras.sort()
print(compras)
print('-' * 70)
print(f'A lista de compras tem {len(compras)} produtos')
print('-' * 70)